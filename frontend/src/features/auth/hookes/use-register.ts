import { useMutation } from "@tanstack/react-query";
import { RegisterUserSchema } from "../auth.schema";

export function useRegister() {
  return useMutation<void, Error, RegisterUserSchema>({
    mutationFn: async (data: RegisterUserSchema) => {
      console.table(data);
    },
  });
}
