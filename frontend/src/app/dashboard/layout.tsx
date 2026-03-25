import { requireAuth } from "@/features/auth/auth.utilts";

export default async function Layout({
  admin,
  tenant,
}: Readonly<{ admin: React.ReactNode; tenant: React.ReactNode }>) {
  const user = await requireAuth();

  const isAdmin = user.roles.some((role) => role.name === "admin");

  return isAdmin ? admin : tenant;
}
