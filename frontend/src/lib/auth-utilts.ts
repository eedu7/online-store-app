import { redirect } from "next/navigation";
import { buildUrl } from "./api/api.utils";
import { cookies } from "next/headers";

export async function requireAuth() {
  const cookieStore = await cookies();
  const cookieHeader = cookieStore.toString();

  const response = await fetch(buildUrl("/users/me"), {
    method: "GET",
    headers: {
      Cookie: cookieHeader,
    },
  });

  if (!response.ok) {
    redirect("/login");
  }
  return response.json();
}

export async function requireUnAuth() {
  const cookieStore = await cookies();
  const cookieHeader = cookieStore.toString();

  const response = await fetch(buildUrl("/users/me"), {
    method: "GET",
    headers: {
      Cookie: cookieHeader,
    },
  });

  if (response.ok) {
    redirect("/");
  }
  return response.json();
}
