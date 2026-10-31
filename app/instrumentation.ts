import { Instrumentation } from "next"

export async function register() {
  // await import("@/lib/envars")
  // await import("@/lib/cache")
  // await import("@/lib/db")
}

export const onRequestError: Instrumentation.onRequestError = (err, req, ctx) => {
  console.log(`====================================================================================================`)
  console.log(`err: ${err}`)
}
