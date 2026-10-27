"use client"

import { launchCodes } from "@/commands/users";
import { useAuth } from "@/context/AuthContext";
import { useCallback } from "react";

export default function Home() {
  const { loggedIn, authRequest } = useAuth()

  const click = useCallback(async () => {
    const lc = await authRequest((token) => launchCodes(token))
    alert(lc)
  }, [authRequest])

  return (
    <div>
      <h2>home</h2>
      {loggedIn && <h1>logged in</h1>}
      <button onClick={click}>get launch codes</button>
    </div>
  );
}
