"use client";

import { useMutation } from "@tanstack/react-query";
import { LoginUserSchema } from "../auth.schema";
import { useRouter } from "next/navigation";

export function useLogin() {
  const router = useRouter();
  return useMutation<void, Error, LoginUserSchema>({
    mutationFn: async (data) => {
      const res = await fetch(
        `${process.env.NEXT_PUBLIC_API_BASE_URL}/api/v1/auth/login`,
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
        throw new Error(error || "Login failed");
      }

      return res.json();
    },
    onSuccess: (data) => {
      console.table(data);
      router.replace("/");
    },
  });
}
