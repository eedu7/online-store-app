import { LoginPage } from "@/features/auth/pages/login-page";
import { requireUnAuth } from "@/lib/auth-utilts";

export default async function Page() {
  await requireUnAuth();
  return <LoginPage />;
}
