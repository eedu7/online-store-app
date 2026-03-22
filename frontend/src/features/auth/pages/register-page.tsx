"use client";

import { RegisterForm } from "../components/register-form";
import { useRegister } from "../hookes/use-register";
import { AuthCard } from "../components/auth-card";

export const RegisterPage = () => {
  const mutation = useRegister();
  return (
    <AuthCard
      title=""
      description=""
      children={<RegisterForm mutation={mutation} />}
    />
  );
};
