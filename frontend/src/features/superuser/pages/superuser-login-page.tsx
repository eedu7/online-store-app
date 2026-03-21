import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { SuperuserLoginForm } from "../components/superuser-login-form";

export const SuperuserLoginPage = () => {
  return (
    <div className="w-full h-screen flex items-center justify-center">
      <Card className="min-w-md max-w-lg">
        <CardHeader>
          <CardTitle></CardTitle>
          <CardDescription></CardDescription>
        </CardHeader>
        <CardContent>
          <SuperuserLoginForm />
        </CardContent>
        <CardFooter></CardFooter>
      </Card>
    </div>
  );
};
