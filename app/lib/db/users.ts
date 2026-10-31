"server only"

import { sql, eq } from "drizzle-orm"
import { NodePgTransaction } from "drizzle-orm/node-postgres"

import { DB, users } from "./schema"
import { AccessToken, createAccessToken, FullUser } from "../views"


export async function createUser(db: DB, user: typeof users.$inferInsert): Promise<AccessToken> {
  const [newUser] = await db.insert(users).values(user).returning({
    id: users.id,
    username: users.username,
    createdAt: users.createdAt
  })

  return createAccessToken(newUser)
}

export async function usernameTaken(db: DB, username: string): Promise<boolean> {
  let q = db.select({ dummy: sql`1` })
    .from(users)
    .where(eq(users.username, username))
    .limit(1)
    .$dynamic()

  if (db instanceof NodePgTransaction)
    q = q.for("update")

  return (await q).length === 1
}

export async function getUserByUsername(db: DB, username: string): Promise<FullUser | undefined> {
  return await db.query.users.findFirst({
    columns: {
      id: true,
      username: true,
      passwordHash: true,
      passwordSalt: true,
      createdAt: true,
    },
    where: {
      username: username,
    }
  })
}
