"use client";

import { useFieldContext } from "@/context/form";
import { useStore } from "@tanstack/react-form";
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { InputHTMLAttributes } from "react";

interface Props extends InputHTMLAttributes<HTMLInputElement> {
  label: string;
}

export const TextField = ({ label, ...props }: Props): React.JSX.Element => {
  const field = useFieldContext<string>();

  const errors = useStore(field.store, (state) => state.meta.errors);

  return (
    <Field>
      <FieldLabel>{label}</FieldLabel>
      <Input
        value={field.state.value}
        onChange={(e) => field.handleChange(e.target.value)}
        onBlur={field.handleBlur}
        {...props}
      />
      {errors.map((error: string) => (
        <FieldDescription key={error} className="text-rose-500">
          {JSON.stringify(error, null, 2)}
        </FieldDescription>
      ))}
    </Field>
  );
};
