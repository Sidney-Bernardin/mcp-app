import Link from "next/link";

export default async function NavBar() {
  const user = false

  return (
    <nav
      className="
        flex justify-around bg-bg-a
        *:flex-1 *:flex *:gap-2 *:justify-center
      "
    >
      {user && <div>username</div>}
      <h1>Rollbringer</h1>
      <ul>
        <li><Link href="/">home</Link></li>
        {
          !user &&
          <li><Link href="/signup">login</Link></li>
        }
      </ul>
    </nav>
  )
}
