import {
  NavigationMenu,
  NavigationMenuList,
} from "@/components/ui/navigation-menu";
import { getCurrentUser } from "@/features/auth/auth.utilts";
import { NavbarDashboardLink } from "@/features/navbar/components/navbar-dashboard-link";
import { NavbarLink } from "@/features/navbar/components/navbar-link";
import { NavbarSignOutButton } from "@/features/navbar/components/navbar-sign-out-button";

export const Navbar = async () => {
  const { authenticated } = await getCurrentUser();

  return (
    <div className="w-full flex justify-end items-center max-w-7xl">
      <NavigationMenu>
        <NavigationMenuList>
          <NavbarLink href="/" label="Home" />
          <NavbarDashboardLink />
          {authenticated ? (
            <NavbarSignOutButton />
          ) : (
            <>
              <NavbarLink href="/login" label="Sign In" />
              <NavbarLink href="/register" label="Sign Up" />
            </>
          )}
        </NavigationMenuList>
      </NavigationMenu>
    </div>
  );
};
