import { getCurrentUser } from "@/features/auth/auth.utilts";
import { NavbarLink } from "@/features/navbar/components/navbar-link";

export const NavbarDashboardLink = async () => {
  const { isAdmin } = await getCurrentUser();
  if (!isAdmin) return null;
  return <NavbarLink href="/dashboard" label="Dashboard" />;
};
