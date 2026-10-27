"use client"

import { useCallback } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";

import { useAuth } from "@/context/AuthContext";

export default function NavBarLinks() {
  const { loggedIn } = useAuth()
  const pathname = usePathname()

  const fromURL = useCallback((href: string) => {
    const hrefURL = new URL(href.toString(), "http://placeholder.com")
    hrefURL.searchParams.set("from", pathname)
    return hrefURL.pathname + hrefURL.search + hrefURL.hash
  }, [pathname])

  return (
    <ul>
      <li><Link href="/?abc=123">home</Link></li>
      {
        !loggedIn &&
        <li><Link href={fromURL("/signup")}>login</Link></li>
      }
    </ul>
  )
}
