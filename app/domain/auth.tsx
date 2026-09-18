import * as z from "zod"

export function refreshToken() {

}

const signupFormSchema = z.object({
  username: z.string().max(32, "Username must be at most 32 characters."),
  password: z.string().min(8, "Password must be at least 8 characters.").trim(),
})

type SignupForm = z.infer<typeof signupFormSchema>
type SignupFormErrors = z.core.$ZodFlattenedError<SignupForm>["fieldErrors"]
export type SignupRes = SignupFormErrors | undefined

export function signup(formData: FormData): SignupRes {
  const form = signupFormSchema.safeParse(formData.entries())
  if (form.error) {
    return z.flattenError(form.error).fieldErrors
  }
}

export function signin() {

}

export function logout() {

}
