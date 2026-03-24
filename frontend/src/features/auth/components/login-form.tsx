"use client";

import { Field, FieldGroup, FieldSet } from "@/components/ui/field";
import { useAppForm } from "@/hooks/form";
import { LoginUserSchema, loginUserSchema } from "../auth.schema";
import { UseMutationResult } from "@tanstack/react-query";
import { revalidateLogic } from "@tanstack/react-form";

interface Props {
  mutation: UseMutationResult<void, Error, LoginUserSchema>;
}

export const LoginForm = ({ mutation }: Props) => {
  const form = useAppForm({
    defaultValues: {
      username_or_email: "",
      password: "",
    },
    validationLogic: revalidateLogic(),
    validators: {
      onDynamic: loginUserSchema,
    },
    onSubmit: async ({ value }) => {
      try {
        mutation.mutateAsync(value);
      } catch {
        // Error is accessbile via mutation.isError / mutation.error
      }
    },
  });
  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        e.stopPropagation();
        form.handleSubmit();
      }}
    >
      <FieldGroup>
        <FieldSet>
          <FieldGroup>
            <form.AppField
              name="username_or_email"
              children={(field) => (
                <field.TextField
                  label="Username or Email"
                  name="username"
                  autoComplete="username email"
                  autoCapitalize="none"
                  spellCheck="false"
                />
              )}
            />

            <form.AppField
              name="password"
              children={(field) => (
                <field.PasswordField
                  label="Password"
                  name="password"
                  autoComplete="new-password"
                />
              )}
            />
          </FieldGroup>
        </FieldSet>
        <Field orientation="horizontal">
          <form.AppForm>
            <form.SubmitButton label="Login" isPending={mutation.isPending} />
          </form.AppForm>
        </Field>
      </FieldGroup>
    </form>
  );
};
