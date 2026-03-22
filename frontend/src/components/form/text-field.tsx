"use client";

import { useFieldContext } from "@/context/form";
import { useStore } from "@tanstack/react-form";
import { Field, FieldLabel } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { InputHTMLAttributes } from "react";
import { FormFieldError } from "./form-field-error";

interface Props extends InputHTMLAttributes<HTMLInputElement> {
  label: string;
  required?: boolean;
}

export const TextField = ({
  label,
  required = false,
  ...props
}: Props): React.JSX.Element => {
  const field = useFieldContext<string>();

  const errors = useStore(field.store, (state) => state.meta.errors);

  return (
    <Field>
      <FieldLabel className="gap-1">
        {label}
        {required && <span className="text-rose-700">*</span>}
      </FieldLabel>
      <Input
        value={field.state.value}
        onChange={(e) => field.handleChange(e.target.value)}
        onBlur={field.handleBlur}
        {...props}
      />
      <FormFieldError errors={errors} />
    </Field>
  );
};
