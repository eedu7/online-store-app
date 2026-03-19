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
import { Input } from "@/components/ui/input";

export const SuperuserRegisterForm = () => {
  return (
    <form>
      <FieldGroup>
        <FieldSet>
          <FieldLegend>Register Title</FieldLegend>
          <FieldDescription>Register Description</FieldDescription>
          <FieldGroup>
            <Field>
              <FieldLabel>First Name</FieldLabel>
              <Input />
            </Field>
            <Field>
              <FieldLabel>Last Name</FieldLabel>
              <Input />
            </Field>
            <Field>
              <FieldLabel>Username</FieldLabel>
              <Input required aria-required />
            </Field>
            <Field>
              <FieldLabel>Email</FieldLabel>
              <Input required aria-required />
            </Field>
            <Field>
              <FieldLabel>Password</FieldLabel>
              <Input required aria-required />
            </Field>
            <Field>
              <FieldLabel>Confirm Password</FieldLabel>
              <Input required aria-required />
            </Field>
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
