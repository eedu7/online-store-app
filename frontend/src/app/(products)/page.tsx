import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export default function Home() {
  return (
    <div className="h-full flex flex-col items-center justify-center">
      <Card className="w-md max-w-lg border-none outline-none ring-0">
        <CardHeader>
          <CardTitle>Online Store</CardTitle>
          <CardDescription></CardDescription>
        </CardHeader>
        <CardContent></CardContent>
        <CardFooter></CardFooter>
      </Card>
    </div>
  );
}
