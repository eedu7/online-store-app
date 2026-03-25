import { RegisterPage } from "@/features/auth/pages/register-page";
import { requireUnAuth } from "@/lib/auth-utilts";

export default async function Page() {
  await requireUnAuth();
  return <RegisterPage />;
}
