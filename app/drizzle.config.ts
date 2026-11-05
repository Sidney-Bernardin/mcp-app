import "dotenv/config"
import { defineConfig } from "drizzle-kit"

export default defineConfig({
  out: "../services/postgres/migrations",
  schema: "./lib/db/schema.ts",
  dialect: "postgresql",
  dbCredentials: {
    url: process.env.POSTGRES_URL!,
  }
})
