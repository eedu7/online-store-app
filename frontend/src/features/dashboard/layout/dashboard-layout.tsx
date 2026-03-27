import { notFound } from "next/navigation";
import type { ReactNode } from "react";
import { getCurrentUser } from "@/features/auth/auth.utilts";

export const DashboardLayout = async ({
  admin,
  tenant,
}: {
  admin: ReactNode;
  tenant: ReactNode;
}) => {
  const { isAdmin, isTenant } = await getCurrentUser();

  if (isAdmin) return admin;
  if (isTenant) return tenant;
  return notFound();
};
