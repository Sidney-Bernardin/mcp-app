import { Suspense } from "react";
import Link from "next/link";

import SigninForm from "@/components/SigninForm";


export default async function Signin() {
  return (
    <div>
      <h1>Signin</h1>
      <Link className="underline" href="/signup" replace>
        signup
      </Link>
      <Suspense fallback={<p>signinform...</p>}>
        <SigninForm />
      </Suspense>
    </div >
  )
}
