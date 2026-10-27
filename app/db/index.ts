import "dotenv/config"
import { sql } from "drizzle-orm"
import { drizzle } from "drizzle-orm/node-postgres"
import { relations } from "./schema"

export const db = drizzle(process.env.POSTGRES_URL!, { relations })
await db.execute(sql`SELECT 1`)
