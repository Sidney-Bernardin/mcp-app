import * as z from "zod"
import { users } from "./db/schema"


export type FormError<T> = {
  fieldErrors?: z.core.$ZodFlattenedError<T>["fieldErrors"]
  formErrors?: string[]
}


export type FullUser = typeof users.$inferSelect
export type OptionalUser = Partial<FullUser>


export type AccessToken = {
  userId: FullUser["id"],
  username: FullUser["username"],
  createdAt: string
}

export function createAccessToken(user: OptionalUser & Pick<FullUser, "id" | "username" | "createdAt">): AccessToken {
  return {
    userId: user.id,
    username: user.username,
    createdAt: user.createdAt.toISOString(),
  }
}
