import Link from "next/link";
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu";

export const Navbar = () => {
  return (
    <NavigationMenu>
      <NavigationMenuList>
        <NavigationLink href="/" label="Home" />
        <NavigationLink href="/login" label="Sign In" />
        <NavigationLink href="/register" label="Sign Up" />
      </NavigationMenuList>
    </NavigationMenu>
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
