import { Suspense } from "react";
import Link from "next/link";

import SignupForm from "@/components/SignupForm";


export default async function Signup() {
  return (
    <div>
      <h1>Signup</h1>
      <Link className="underline" href="/signin" replace>
        signin
      </Link>
      <Suspense fallback={<p>signupform...</p>}>
        <SignupForm />
      </Suspense>
    </div>
  )
}
