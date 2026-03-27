import { Navbar } from "@/features/navbar/components/navbar";

export const ProductLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="h-screen w-full flex flex-col">
      <div className="w-full flex justify-end items-center max-w-7xl">
        <Navbar />
      </div>
      <main className="flex-1">{children}</main>
    </div>
  );
};
