"use client";
import { useMutation } from "@tanstack/react-query";
import { useRouter } from "next/navigation";
import { apiBrowserClient } from "@/lib/api/api.client";

export function useLogout() {
  const router = useRouter();
  return useMutation({
    mutationFn: async () => {
      await apiBrowserClient("/auth/logout", {
        body: JSON.stringify({
          access_token: null,
          refresh_token: null,
        }),
        method: "POST",
      });
    },
    mutationKey: ["use-logout", "use-auth"],
    onSuccess: () => {
      router.push("/login");
    },
  });
}
