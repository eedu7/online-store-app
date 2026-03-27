import { redirect } from "next/navigation";
import { cache } from "react";
import { ApiError } from "@/lib/api/api.error";
import { apiServerClient } from "@/lib/api/api.server";
import type { CurrentUser, User } from "./auth.type";

function hasRole(user: User, role: string): boolean {
  return user.roles.some((r) => r.name.toLowerCase() === role.toLowerCase());
}

const GUEST: CurrentUser = {
  authenticated: false,
  isAdmin: false,
  isCustomer: false,
  isTenant: false,
  user: null,
};

function buildCurrentUser(user: User): CurrentUser {
  return {
    authenticated: true,
    isAdmin: hasRole(user, "admin"),
    isCustomer: true,
    isTenant: hasRole(user, "tenant"),
    user,
  };
}

export const getCurrentUser = cache(async (): Promise<CurrentUser> => {
  try {
    const user: User = await apiServerClient("/users/me");
    return buildCurrentUser(user);
  } catch (error) {
    if (
      error instanceof ApiError &&
      (error.status === 401 || error.status === 403)
    ) {
      return GUEST;
    }
    throw error;
  }
});

export async function requireAuth() {
  const { authenticated } = await getCurrentUser();
  if (!authenticated) redirect("/login");
}

export async function requireUnAuth() {
  const { authenticated } = await getCurrentUser();
  if (authenticated) redirect("/");
}
