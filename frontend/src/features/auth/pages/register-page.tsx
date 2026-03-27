import {AuthCard} from "../components/auth-card";
import {RegisterForm} from "../components/register-form";

export const RegisterPage = async () => {
  return (
    <AuthCard description="Sign up to get started" title="Create an account">
      <RegisterForm />
    </AuthCard>
  );
};
