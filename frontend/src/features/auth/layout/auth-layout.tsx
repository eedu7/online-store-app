import type { ReactNode } from "react";
import { requireUnAuth } from "@/features/auth/auth.utilts";
import { Navbar } from "@/features/navbar/components/navbar";

export const AuthLayout = async ({ children }: { children: ReactNode }) => {
  await requireUnAuth();
  return (
    <div className="w-full h-screen flex flex-col ">
      <Navbar />
      <main className="flex-1 h-full flex items-center justify-center">
        {children}
      </main>
    </div>
  );
};
