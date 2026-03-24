"use client";
import { useMutation } from "@tanstack/react-query";
import { RegisterUserSchema } from "../auth.schema";
import { useRouter } from "next/navigation";
import { AuthResponse } from "../auth.type";
import { useAuthStore } from "../auth.store";

export function useRegister() {
  const router = useRouter();
  const setToken = useAuthStore((state) => state.setToken);

  return useMutation<AuthResponse, Error, RegisterUserSchema>({
    mutationFn: async (data) => {
      const res = await fetch(
        `${process.env.NEXT_PUBLIC_API_BASE_URL}/api/v1/auth/register`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        },
      );

      if (!res.ok) {
        const error = await res.text();
        throw new Error(error || "Registration failed");
      }

      return res.json();
    },
    onSuccess: (data) => {
      setToken(data.token.access_token, data.token.refresh_token);
      router.replace("/");
    },
  });
}
