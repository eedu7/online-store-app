"use client";
import { useMutation } from "@tanstack/react-query";
import { RegisterUserSchema } from "../auth.schema";
import { useRouter } from "next/navigation";
import { AuthResponse } from "../auth.type";
import { useAuthStore } from "../auth.store";
import { apiBrowserClient } from "@/lib/api/api.client";

export function useRegister() {
  const router = useRouter();
  const setToken = useAuthStore((state) => state.setToken);

  return useMutation<AuthResponse, Error, RegisterUserSchema>({
    mutationKey: ["use-register", "auth"],
    mutationFn: async (data) =>
      await apiBrowserClient("/auth/register", {
        method: "POST",
        body: JSON.stringify(data),
      }),
    onSuccess: (data) => {
      setToken(data.token.access_token, data.token.refresh_token);
      router.replace("/");
    },
  });
}
