import { RegisterForm } from "../components/register-form";
import { AuthCard } from "../components/auth-card";
import { requireUnauth } from "@/features/auth/auth.utilts";

export const RegisterPage = async () => {
  await requireUnauth();
  return <AuthCard title="" description="" children={<RegisterForm />} />;
};
