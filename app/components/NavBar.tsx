import NavBarLinks from "@/components/NavBarLinks";
import { Suspense } from "react";

export default function NavBar() {
  return (
    <nav
      className="
        flex justify-around bg-bg-a
        *:flex-1 *:flex *:gap-2 *:justify-center
      "
    >
      <h1>Rollbringer</h1>
      <Suspense fallback={<p>buttons...</p>}>
        <NavBarLinks />
      </Suspense>
    </nav>
  )
}
