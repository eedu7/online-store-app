import z from "zod";

export const loginSchema = z.object({
  username_or_email: z.string().min(1),
  password: z.string(),
});

export const registerUserSchema = z
  .object({
    username: z
      .string()
      .min(3, "Username must be at least 3 characters long.")
      .max(30, "Username must not exceed 30 characters."),
    email: z.email(),
    password: z
      .string()
      .min(8, "Password must be at least 8 characters long.")
      .regex(/[A-Z]/, "Password must contain at least one uppercase letter.")
      .regex(/[a-z]/, "Password must contain at least one lowercase letter.")
      .regex(/[0-9]/, "Password must contain at least one number.")
      .regex(
        /[^A-Za-z0-9]/,
        "Password must contain at least one special character.",
      ),
    confirmPassword: z.string().min(1, "Confirm Password is required."),
  })
  .superRefine(({ password, confirmPassword }, ctx) => {
    if (confirmPassword !== password) {
      ctx.addIssue({
        code: "custom",
        message: "The passwords does not match",
        path: ["confirmPassword"],
      });
    }
  });

export type RegisterUserSchema = z.infer<typeof registerUserSchema>;
