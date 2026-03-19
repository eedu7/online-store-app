"use client";

import { Button } from "@/components/ui/button";
import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSet,
} from "@/components/ui/field";
import { useAppForm } from "@/hooks/form";

export const SuperuserRegisterForm = () => {
  const form = useAppForm({
    defaultValues: {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    },
  });
  return (
    <form>
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
          <Button type="submit">Submit</Button>
          <Button variant="outline" type="button">
            Cancel
          </Button>
        </Field>
      </FieldGroup>
    </form>
  );
};
