"use client";

import { Button } from "@/components/ui/button";
import { NavigationMenuItem } from "@/components/ui/navigation-menu";
import { Spinner } from "@/components/ui/spinner";
import { useLogout } from "@/features/auth/hooks/use-logout";

export const NavbarSignOutButton = () => {
  const logout = useLogout();

  return (
    <NavigationMenuItem>
      <Button
        disabled={logout.isPending}
        onClick={() => logout.mutate()}
        variant="ghost"
      >
        {logout.isPending ? (
          <>
            <Spinner /> Signing out
          </>
        ) : (
          "Sign Out"
        )}
      </Button>
    </NavigationMenuItem>
  );
};
