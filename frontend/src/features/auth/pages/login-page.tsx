import { requireUnauth } from "@/features/auth/auth.utilts";
import { AuthCard } from "../components/auth-card";
import { LoginForm } from "../components/login-form";

export const LoginPage = async () => {
  await requireUnauth();
  return <AuthCard title="" description="" children={<LoginForm />} />;
};
