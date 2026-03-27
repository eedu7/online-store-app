import {redirect} from "next/navigation";
import {apiServerClient} from "@/lib/api/api.server";
import type {CurrentUser, User} from "./auth.type";

export async function requireAuth(): Promise<User> {
  try {
    return await apiServerClient("/users/me");
  } catch {
    redirect("/login");
  }
}

export async function requireUnauth() {
  try {
    await apiServerClient("/users/me");
    redirect("/");
  } catch {
    // Not authenticated, allow access
  }
}

function hasRole(user: User, role: string): boolean {
  return user.roles.some((r) => r.name.toLowerCase() === role.toLowerCase());
}

export async function getCurrentUser(): Promise<CurrentUser> {
  try {
    const user = await apiServerClient("/users/me");
    return {
      isAdmin: hasRole(user, "admin"),
      isCustomer: hasRole(user, "customer"),
      isTenant: hasRole(user, "tenant"),
      user,
    };
  } catch {
    return {
      isAdmin: false,
      isCustomer: false,
      isTenant: false,
      user: null,
    };
  }
}
