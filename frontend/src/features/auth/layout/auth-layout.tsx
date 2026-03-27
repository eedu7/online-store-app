import type { ReactNode } from "react";
import { Navbar } from "@/features/navbar/components/navbar";

export const AuthLayout = ({ children }: { children: ReactNode }) => {
  return (
    <div className="w-full h-screen flex flex-col ">
      <Navbar />
      <main className="flex-1 h-full flex items-center justify-center">
        {children}
      </main>
    </div>
  );
};
