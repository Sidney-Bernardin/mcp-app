import { z } from "zod"

const envarsSchema = z.object({
  SECRET: z.string(),

  POSTGRES_URL: z.url(),
  REDIS_URL: z.url(),

  REFRESH_TOKEN_EXPIRATION_SECONDS: z.coerce.number(),
  ACCESS_TOKEN_EXPIRATION_SECONDS: z.coerce.number(),
})

const envars_ = envarsSchema.safeParse(process.env)
if (!envars_.success)
  throw Error(envars_.error.message)

export const envars = envars_.data
