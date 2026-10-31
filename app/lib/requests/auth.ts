"use server"

import { cookies } from "next/headers"

import crypto from "crypto"
import * as JWT from "jsonwebtoken"
import * as z from "zod"

import { Result } from "@/lib/errors"
import { envars } from "@/lib/envars"
import { AccessToken, createAccessToken, FormError } from "@/lib/views"
import { db } from "@/lib/db"
import { createUser, getUserByUsername, usernameTaken } from "@/lib/db/users"
import { getSession, setSession } from "../cache/queries"
import { SigninForm, signinFormSchema, SignupForm, signupFormSchema } from "../commands"

export async function refresh(): Promise<string | undefined> {
  const cookieStore = await cookies()

  const refreshToken = cookieStore.get("refreshToken")
  if (!refreshToken)
    return undefined

  const accessToken = await getSession(refreshToken.value)
  return signAccessToken(accessToken)
}

export async function signup(formData: FormData): Promise<Result<string, FormError<SignupForm>>> {

  // Validate form.
  const form = signupFormSchema.safeParse(Object.fromEntries(formData.entries()))
  if (form.error)
    return [undefined, z.flattenError(form.error)]

  const [accessToken, err] = await db.transaction(async (tx) => {

    // Check if the username is taken.
    if (await usernameTaken(tx, form.data.username))
      return [undefined, {
        fieldErrors: { username: ["Username taken."] }
      }]

    // Hash password.
    const passwordSalt = crypto.randomBytes(32)
    const passwordHash = await hashUserPassword(form.data.password, passwordSalt)

    // Create user.
    return [await createUser(tx, {
      username: form.data.username,
      passwordHash,
      passwordSalt,
    }), undefined]
  })

  if (err)
    return [undefined, err]

  await createSession(accessToken)
  return [signAccessToken(accessToken), undefined]
}


export async function signin(formData: FormData): Promise<Result<string, FormError<SigninForm>>> {

  const form = signinFormSchema.safeParse(Object.fromEntries(formData.entries()))
  if (form.error) {
    return [undefined, z.flattenError(form.error)]
  }

  const user = await getUserByUsername(db, form.data.username)

  // Check if user doesn't exist or a password mismatch.
  if (!user || !crypto.timingSafeEqual(user.passwordHash, await hashUserPassword(form.data.password, user.passwordSalt)))
    return [undefined, {
      fieldErrors: { username: ["That user doesn't exist."] },
    }]

  const accessToken = createAccessToken(user)
  await createSession(accessToken)
  return [signAccessToken(accessToken), undefined]
}

async function createSession(accessToken: AccessToken) {
  const refreshToken = crypto.randomUUID()

  setSession(refreshToken, accessToken)

  const cookieStore = await cookies()
  cookieStore.set("refreshToken", refreshToken, {
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

async function hashUserPassword(pw: string, salt: Buffer): Promise<Buffer> {
  return new Promise<Buffer>((resolve, reject) => {
    crypto.scrypt(pw.normalize(), salt, 64, (err, hash) => {
      if (err) reject(err)
      else resolve(hash)
    })
  })
}
