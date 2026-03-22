import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { RegisterForm } from "@/features/auth/components/register-form";

export const SuperuserRegisterPage = () => {
  return (
    <div className="w-full h-screen flex items-center justify-center">
      <Card className="min-w-md max-w-lg">
        <CardHeader>
          <CardTitle></CardTitle>
          <CardDescription></CardDescription>
        </CardHeader>
        <CardContent>
          <RegisterForm />
        </CardContent>
        <CardFooter></CardFooter>
      </Card>
    </div>
  );
};
