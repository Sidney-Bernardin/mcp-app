"use client"

import { signup, SignupRes } from "@/domain/auth"
import Form from "next/form"
import { useActionState } from "react"

export default function Signup() {
  const [state, signupAction, loading] = useActionState(
    (_prevState: SignupRes, form: FormData) => signup(form),
    undefined,
  )

  return (
    <Form action={signupAction}>
      <input name="username" type="text" placeholder="Username" disabled={loading} />
      <input name="password" type="password" placeholder="Password" disabled={loading} />
      <input type="submit" disabled={loading} />
    </Form>
  )
}
