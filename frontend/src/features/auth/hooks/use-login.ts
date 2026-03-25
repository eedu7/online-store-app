"use client";

import { useMutation } from "@tanstack/react-query";
import { LoginUserSchema } from "../auth.schema";
import { useRouter } from "next/navigation";
import { AuthResponse } from "../auth.type";
import { useAuthStore } from "../auth.store";
import { apiBrowserClient } from "@/lib/api/api.client";

export function useLogin() {
  const router = useRouter();
  const setToken = useAuthStore((state) => state.setToken);

  return useMutation<AuthResponse, Error, LoginUserSchema>({
    mutationKey: ["use-login", "auth"],
    mutationFn: async (data) =>
      await apiBrowserClient("/auth/login", {
        method: "POST",
        body: JSON.stringify(data),
      }),
    onSuccess: (data) => {
      setToken(data.token.access_token, data.token.refresh_token);
      router.replace("/");
    },
  });
}
