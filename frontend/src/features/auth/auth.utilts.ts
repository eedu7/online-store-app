import {redirect} from "next/navigation";
import {apiServerClient} from "@/lib/api/api.server";
import type {UserResponse} from "./auth.type";

export async function requireAuth(): Promise<UserResponse> {
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

export async function getCurrentUser(): Promise<UserResponse | null> {
  try {
    return await apiServerClient("/users/me");
  } catch {
    return null;
  }
}
