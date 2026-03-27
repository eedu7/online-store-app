import Link from "next/link";
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu";
import {getCurrentUser} from "@/features/auth/auth.utilts";
import {NavbarSignOutButton} from "@/features/navbar/components/navbar-sign-out-button";

export const Navbar = async () => {
  const currentUser = await getCurrentUser();

  return (
    <div className="w-full flex justify-end items-center max-w-7xl">
      <NavigationMenu>
        <NavigationMenuList>
          <NavigationLink href="/" label="Home" />
          {currentUser ? (
            <NavbarSignOutButton />
          ) : (
            <>
              <NavigationLink href="/login" label="Sign In" />
              <NavigationLink href="/register" label="Sign Up" />
            </>
          )}
        </NavigationMenuList>
      </NavigationMenu>
    </div>
  );
};

interface NavigationLinkProps {
  href: string;
  label: string;
}

const NavigationLink = ({ label, href }: NavigationLinkProps) => {
  return (
    <NavigationMenuItem>
      <NavigationMenuLink
        className={navigationMenuTriggerStyle()}
        render={<Link href={href}>{label}</Link>}
      />
    </NavigationMenuItem>
  );
};
