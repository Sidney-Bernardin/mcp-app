import * as z from "zod"

export type FormError<T> = {
  fieldErrors?: z.core.$ZodFlattenedError<T>["fieldErrors"]
  formErrors?: string[]
}

export const signupFormSchema = z.object({
  username: z.string()
    .min(3, "Username must be at least 3 characters.")
    .max(32, "Username must be at most 32 characters."),
  password: z.string()
    .min(3, "Password must be at least 3 characters.").trim(),
})

export type SignupForm = z.infer<typeof signupFormSchema>


export const signinFormSchema = z.object({
  username: z.string(),
  password: z.string().trim(),
})

export type SigninForm = z.infer<typeof signinFormSchema>
