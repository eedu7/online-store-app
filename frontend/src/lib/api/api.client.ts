import { ApiError } from "./api.error";
import { buildUrl } from "./api.utils";

export async function apiBrowserClient(endpoint: string, init?: RequestInit) {
  const res = await fetch(buildUrl(endpoint), {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...init?.headers,
    },
    credentials: "include",
  });
  if (!res.ok) {
    const body = await res.json();
    throw new ApiError(res.status, body.detail);
  }
  return res.json();
}
