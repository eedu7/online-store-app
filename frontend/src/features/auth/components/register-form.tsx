"use client";

import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLegend,
  FieldSet,
} from "@/components/ui/field";
import { useAppForm } from "@/hooks/form";
import { registerUserSchema } from "../auth.schema";

export const RegisterForm = () => {
  const form = useAppForm({
    defaultValues: {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    },
    validators: {
      onDynamic: registerUserSchema,
    },
    onSubmit: async ({ value }) => {
      console.log(value);
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
          <FieldLegend>Register Title</FieldLegend>
          <FieldDescription>Register Description</FieldDescription>
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
            <form.SubmitButton label="Register" />
          </form.AppForm>
        </Field>
      </FieldGroup>
    </form>
  );
};
