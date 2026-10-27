"server only"

import { createClient } from "redis";
import envars from "@/envars";

export const redis = await createClient({ url: envars.REDIS_URL }).connect()
await redis.ping()
