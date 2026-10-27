import { Instrumentation } from "next"

// export async function register() {
//   await import("@/envars")
//   await import("@/redis")
//   await import("@/db")
// }

export const onRequestError: Instrumentation.onRequestError = (err, req, ctx) => {
  console.log(`====================================================================================================`)
  console.log(`err: ${err}`)
}
