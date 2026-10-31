"server only"

import { sql } from "drizzle-orm"
import { drizzle } from "drizzle-orm/node-postgres"

import { envars } from "@/lib/envars"

import { relations } from "./schema"


export const db = drizzle(envars.POSTGRES_URL, { relations })
await db.execute(sql`SELECT 1`)

