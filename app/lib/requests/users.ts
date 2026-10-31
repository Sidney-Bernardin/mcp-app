"use server"

export async function launchCodes(accessToken: string | undefined) {
  if (!accessToken) return "unauthorized!"
  return "123421424"
}
