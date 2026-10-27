import { NextRequest, NextResponse } from "next/server";

const privateRoutes = [
  "/secret"
]

export function middleware(req: NextRequest) {
  if (!req.cookies.has("refreshToken") && privateRoutes.some((route) => req.nextUrl.pathname.startsWith(route)))
    return NextResponse.redirect("/signup")

  return NextResponse.next()
}
