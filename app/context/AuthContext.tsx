"use client"

import { createContext, Dispatch, ReactNode, SetStateAction, use, useCallback, useEffect, useState } from "react";
import * as JWT from "jsonwebtoken"
import { refresh } from "@/commands/auth";

interface AuthContextType {
  loggedIn: boolean
  setAccessToken: Dispatch<SetStateAction<string | undefined>>
  authRequest: <T>(doReq: (accessToken: string | undefined) => T) => Promise<T>
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export function AuthProvider(props: { children: ReactNode }) {
  const [accessToken, setAccessToken] = useState<string | undefined>(undefined)
  const loggedIn = accessToken !== undefined

  const authRequest = useCallback(async <T,>(doReq: (accessToken: string | undefined) => T) => {
    if (accessToken) {
      const exp = JWT.decode(accessToken, { json: true })?.exp
      if (exp && exp * 1000 > Date.now()) // Multiply by 1000 to convert the JWT's seconds into miliseconds.
        return doReq(accessToken)
      console.log("expired")
    }

    const newAccessToken = await refresh()
    setAccessToken(newAccessToken)
    return doReq(newAccessToken)
  }, [accessToken])

  useEffect(() => {
    refresh().then((newAccessToken) => setAccessToken(newAccessToken))
    return () => { }
  }, [])

  return (
    <AuthContext value={{ authRequest, loggedIn, setAccessToken }}>
      {props.children}
    </AuthContext>
  )
}

export function useAuth() {
  const ctx = use(AuthContext)
  if (!ctx)
    throw new Error("No Authprovider")
  return ctx
}
