"use client";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { RegisterForm } from "@/features/auth/components/register-form";
import { useRegister } from "@/features/auth/hookes/use-register";

export const SuperuserRegisterPage = () => {
  const mutation = useRegister();
  return (
    <div className="w-full h-screen flex items-center justify-center">
      <Card className="min-w-md max-w-lg">
        <CardHeader>
          <CardTitle></CardTitle>
          <CardDescription></CardDescription>
        </CardHeader>
        <CardContent>
          <RegisterForm mutation={mutation} />
        </CardContent>
        <CardFooter></CardFooter>
      </Card>
    </div>
  );
};
