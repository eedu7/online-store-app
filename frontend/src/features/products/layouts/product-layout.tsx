import { Navbar } from "@/features/navbar/components/navbar";

export const ProductLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="h-screen w-full flex flex-col">
      <Navbar />
      <main className="flex-1">{children}</main>
    </div>
  );
};
