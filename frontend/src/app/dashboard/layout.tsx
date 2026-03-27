import { notFound } from "next/navigation";
import type { ReactNode } from "react";
import { getCurrentUser } from "@/features/auth/auth.utilts";

export default async function Layout({
  admin,
  tenant,
}: Readonly<{ admin: ReactNode; tenant: ReactNode }>) {
  const { isAdmin, isTenant } = await getCurrentUser();

  if (isAdmin) return admin;
  if (isTenant) return tenant;
  return notFound();
}
