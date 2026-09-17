import Link from "next/link";

export default async function NavBar() {
  return (
    <nav className="bg-bg-b">
      <h1>Rollbringer</h1>
      <ul>
        <li><Link href="/">home</Link></li>
      </ul>
    </nav>
  )
}
