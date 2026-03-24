"use client";

import { AuthCard } from "../components/auth-card";
import { LoginForm } from "../components/login-form";
import { useLogin } from "../hookes/use-login";

export const LoginPage = () => {
  const mutation = useLogin();
  return (
    <AuthCard
      title=""
      description=""
      children={<LoginForm mutation={mutation} />}
    />
  );
};
