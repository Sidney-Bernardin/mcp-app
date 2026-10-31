"server only"

import { envars } from "../envars"
import { AccessToken } from "../views"
import { cache } from "./index"

const key = (refreshToken: string) => `session:${refreshToken}`

export async function setSession(refreshToken: string, accessToken: AccessToken): Promise<void> {
  await cache.multi()
    .hSet(key(refreshToken), accessToken)
    .expire(key(refreshToken), envars.REFRESH_TOKEN_EXPIRATION_SECONDS)
    .exec()
}

export async function getSession(refreshToken: string): Promise<AccessToken> {
  return await cache.hGetAll(key(refreshToken)) as unknown as AccessToken
}
