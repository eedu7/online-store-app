"use client";

import { useMutation } from "@tanstack/react-query";
import { LoginUserSchema } from "../auth.schema";
import { useRouter } from "next/navigation";
import { AuthResponse } from "../auth.type";
import { useAuthStore } from "../auth.store";
import { buildUrl } from "@/lib/utils";

export function useLogin() {
  const router = useRouter();
  const setToken = useAuthStore((state) => state.setToken);

  return useMutation<AuthResponse, Error, LoginUserSchema>({
    mutationFn: async (data) => {
      const res = await fetch(buildUrl("/auth/login"), {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
        credentials: "include",
      });

      if (!res.ok) {
        const error = await res.text();
        throw new Error(error || "Login failed");
      }

      return res.json();
    },
    onSuccess: (data) => {
      setToken(data.token.access_token, data.token.refresh_token);
      router.replace("/");
    },
  });
}
