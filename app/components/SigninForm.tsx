"use client"

import { useActionState } from "react"
import Form from "next/form"

import { signin } from "@/commands/auth"
import { FormError, SigninForm as SigninFormType } from "@/forms/auth"
import { useSearchParams, useRouter } from "next/navigation"
import { useAuth } from "@/context/AuthContext"


export default function SigninForm() {
  const { setAccessToken } = useAuth()
  const router = useRouter()
  const searchParams = useSearchParams()

  const [state, action, pending] = useActionState(
    async (_prev: FormError<SigninFormType> | undefined, formData: FormData) => {
      const [newAccessToken, err] = await signin(formData)
      if (err)
        return err

      setAccessToken(newAccessToken)
      router.push(searchParams.get("from") || "/")
    },
    undefined,
  )

  return (
    <Form action={action}>
      <input name="username" type="text" placeholder="Username" disabled={pending} />
      {state && state.fieldErrors?.username?.map((err, idx) =>
        <p key={idx}>{err}</p>)}

      <input name="password" type="password" placeholder="Password" disabled={pending} />
      {state && state.fieldErrors?.password?.map((err, idx) =>
        <p key={idx}>{err}</p>)}

      <input type="submit" disabled={pending} />
      {state && state.formErrors?.map((err, idx) =>
        <p key={idx}>{err}</p>)}
    </Form>
  )
}
