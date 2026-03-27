import { AuthCard } from "../components/auth-card";
import { LoginForm } from "../components/login-form";

export const LoginPage = async () => {
  return (
    <AuthCard
      description="Login to your account to continue"
      title="Welcome Back"
    >
      <LoginForm />
    </AuthCard>
  );
};
