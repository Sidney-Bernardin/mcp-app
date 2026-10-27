"use server"

import { cookies } from "next/headers"

import crypto from "crypto"
import * as JWT from "jsonwebtoken"
import { eq, sql } from "drizzle-orm"
import * as z from "zod"

import { Result } from "@/errors"
import envars from "@/envars"
import { redis } from "@/redis"
import { db } from "@/db"
import * as schema from "@/db/schema"
import { signupFormSchema, FormError, SignupForm, SigninForm } from "@/forms/auth"

type AccessTokenUser = Pick<schema.FullUser, "id" | "username" | "createdAt">
type AccessToken = Omit<AccessTokenUser, "id" | "createdAt"> & {
  userId: AccessTokenUser["id"],
  createdAt: string
}

export async function refresh(): Promise<string | undefined> {
  const cookieStore = await cookies()

  const refreshToken = cookieStore.get("refreshToken")
  if (!refreshToken)
    return undefined

  const accessTokenPayload = await redis.hGetAll(`refreshTokens:${refreshToken}`) as unknown as AccessToken
  return signAccessToken(accessTokenPayload)
}

export async function signup(formData: FormData): Promise<Result<string, FormError<SignupForm>>> {

  const form = signupFormSchema.safeParse(Object.fromEntries(formData.entries()))
  if (form.error)
    return [undefined, z.flattenError(form.error)]

  const [user, err] = await db.transaction(async (tx) => {
    const exists = await tx.select({ dummy: sql`1` })
      .from(schema.users)
      .where(eq(schema.users.username, form.data.username))
      .limit(1)
      .for("update")

    if (exists.length > 0)
      return [undefined, {
        fieldErrors: { username: ["Username taken."] }
      }]

    const passwordSalt = crypto.randomBytes(32)
    const passwordHash = await hashUserPassword(form.data.password, passwordSalt)

    return [(await tx.insert(schema.users).values({
      username: form.data.username,
      passwordHash,
      passwordSalt,
    }).returning({
      id: schema.users.id,
      username: schema.users.username,
      createdAt: schema.users.createdAt
    }))[0], undefined]
  })

  if (err)
    return [undefined, err]

  const accessToken = accessTokenFromUser(user)
  await createRefreshToken(accessToken)
  return [signAccessToken(accessToken), undefined]
}

export async function signin(formData: FormData): Promise<Result<string, FormError<SigninForm>>> {

  const form = signupFormSchema.safeParse(Object.fromEntries(formData.entries()))
  if (form.error) {
    return [undefined, z.flattenError(form.error)]
  }

  const user = await db.query.users.findFirst({
    columns: {
      id: true,
      username: true,
      passwordHash: true,
      passwordSalt: true,
      createdAt: true,
    },
    where: {
      username: form.data.username,
    }
  })

  // Check if user doesn't exist or a password mismatch.
  if (!user || !crypto.timingSafeEqual(user.passwordHash, await hashUserPassword(form.data.password, user.passwordSalt)))
    return [undefined, {
      fieldErrors: { username: ["That user doesn't exist."] },
    }]

  const accessToken = accessTokenFromUser(user)
  await createRefreshToken(accessToken)
  return [signAccessToken(accessToken), undefined]
}

async function createRefreshToken(accessToken: AccessToken) {

  // Create refresh-token.
  const refreshTokenId = crypto.randomUUID()
  const refreshTokenKey = `refreshTokens:${refreshTokenId}`
  await redis.multi()
    .hSet(refreshTokenKey, accessToken)
    .expire(refreshTokenKey, envars.REFRESH_TOKEN_EXPIRATION_SECONDS)
    .exec()

  // Create refresh-token cookie.
  const cookieStore = await cookies()
  cookieStore.set("refreshToken", refreshTokenId, {
    httpOnly: true,
    secure: true,
    sameSite: "strict",
    path: "/",
    maxAge: envars.REFRESH_TOKEN_EXPIRATION_SECONDS,
  })
}

function signAccessToken(user: AccessToken): string {
  return JWT.sign(user, envars.SECRET, {
    expiresIn: envars.ACCESS_TOKEN_EXPIRATION_SECONDS
  })
}

function accessTokenFromUser(user: schema.OptionalUser & AccessTokenUser): AccessToken {
  return {
    userId: user.id,
    username: user.username,
    createdAt: user.createdAt.toISOString(),
  }
}

async function hashUserPassword(pw: string, salt: Buffer): Promise<Buffer> {
  return new Promise<Buffer>((resolve, reject) => {
    crypto.scrypt(pw.normalize(), salt, 64, (err, hash) => {
      if (err) reject(err)
      else resolve(hash)
    })
  })
}
