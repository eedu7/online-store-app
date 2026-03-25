import { cookies } from "next/headers";
import { buildUrl } from "./api.utils";
import { ApiError } from "./api.error";

export async function apiServerClient(endpoint: string, init?: RequestInit) {
  const cookieStore = await cookies();
  const res = await fetch(buildUrl(endpoint), {
    ...init,
    headers: {
      "Content-Type": "application/json",
      Cookie: cookieStore.toString(),
      ...init?.headers,
    },
  });

  if (!res.ok) {
    const body = await res.json();
    throw new ApiError(res.status, body.detail);
  }
  return res.json();
}
