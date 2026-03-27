import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

interface Props {
  title: string;
  description: string;
  children: React.ReactNode;
}

export const AuthCard = ({ title, description, children }: Props) => {
  return (
    <Card className="w-full max-w-md">
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <CardDescription>{description}</CardDescription>
      </CardHeader>
      <CardContent>{children}</CardContent>
      <CardFooter>
        <TermAndPolicy />
      </CardFooter>
    </Card>
  );
};

const TermAndPolicy = () => {
  return (
    <p className="text-xs text-muted-foreground text-cetner">
      By continuing, you agree to our{" "}
      <span className="underline cursor-pointer">Terms of Service</span> and{" "}
      <span className="underline cursor-pointer">Privacy Policy</span>
    </p>
  );
};
