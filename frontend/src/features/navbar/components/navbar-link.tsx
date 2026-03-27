import Link from "next/link";
import {
  NavigationMenuItem,
  NavigationMenuLink,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu";

interface NavbarLinkProps {
  href: string;
  label: string;
}

export const NavbarLink = ({ label, href }: NavbarLinkProps) => {
  return (
    <NavigationMenuItem>
      <NavigationMenuLink
        className={navigationMenuTriggerStyle()}
        render={<Link href={href}>{label}</Link>}
      />
    </NavigationMenuItem>
  );
};
