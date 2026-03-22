"use client";

import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLegend,
  FieldSet,
} from "@/components/ui/field";
import { useAppForm } from "@/hooks/form";
import { RegisterUserSchema, registerUserSchema } from "../auth.schema";
import { UseMutationResult } from "@tanstack/react-query";
import { revalidateLogic } from "@tanstack/react-form";

interface Props {
  mutation: UseMutationResult<void, Error, RegisterUserSchema>;
}

export const RegisterForm = ({ mutation }: Props) => {
  const form = useAppForm({
    defaultValues: {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    },
    validationLogic: revalidateLogic(),
    validators: {
      onDynamic: registerUserSchema,
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
              name="username"
              children={(field) => (
                <field.TextField
                  label="Username"
                  name="username"
                  autoComplete="username"
                  autoCapitalize="none"
                  spellCheck="false"
                />
              )}
            />
            <form.AppField
              name="email"
              children={(field) => (
                <field.TextField
                  label="Email"
                  name="email"
                  autoComplete="email"
                  autoCapitalize="none"
                  spellCheck="false"
                  type="email"
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
            <form.AppField
              name="confirmPassword"
              children={(field) => (
                <field.PasswordField
                  label="Confirm Password"
                  name="confirmPassword"
                  autoComplete="new-password"
                />
              )}
            />
          </FieldGroup>
        </FieldSet>
        <Field orientation="horizontal">
          <form.AppForm>
            <form.SubmitButton
              label="Register"
              isPending={mutation.isPending}
            />
          </form.AppForm>
        </Field>
      </FieldGroup>
    </form>
  );
};
