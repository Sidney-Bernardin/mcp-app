"use client"

import Link, { type LinkProps } from "next/link"
import { usePathname } from "next/navigation"

interface ClientLinkProps extends LinkProps {
  children: React.ReactNode
  from?: boolean
}

export default function ClientLink({ children, from, ...props }: ClientLinkProps) {
  const pathname = usePathname()

  if (from) {
    const href = new URL(props.href.toString(), "http://placeholder.com")
    href.searchParams.set("from", pathname)
    props.href = href.pathname + href.search + href.hash
  }

  return (
    <Link href={props.href}>
      {children}
    </Link>
  )
}
