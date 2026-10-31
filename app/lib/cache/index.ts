"server only"

import { createClient } from "redis";
import { envars } from "@/lib/envars";

export const cache = await createClient({ url: envars.REDIS_URL }).connect()
await cache.ping()
