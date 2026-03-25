import { redirect } from "next/navigation";
import { apiServerClient } from "@/lib/api/api.server";
import { UserResponse } from "./auth.type";

export async function requireAuth(): Promise<UserResponse> {
  try {
    const user = await apiServerClient("/users/me");
    return user;
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
