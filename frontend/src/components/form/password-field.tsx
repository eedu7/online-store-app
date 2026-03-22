"use client";

import { useFieldContext } from "@/context/form";
import { useStore } from "@tanstack/react-form";
import { Field, FieldError, FieldLabel } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { InputHTMLAttributes, useState } from "react";
import { HugeiconsIcon } from "@hugeicons/react";
import { Eye, EyeOff } from "@hugeicons/core-free-icons";
import { FormFieldError } from "./form-field-error";

interface Props extends InputHTMLAttributes<HTMLInputElement> {
  label: string;
  required?: boolean;
}

export const PasswordField = ({
  label,
  required = false,
  ...props
}: Props): React.JSX.Element => {
  const field = useFieldContext<string>();

  const errors = useStore(field.store, (state) => state.meta.errors);

  const [isVisible, setIsVisible] = useState<boolean>(false);
  const toggleVisibility = () => setIsVisible((prev) => !prev);

  return (
    <Field>
      <FieldLabel className="gap-1">
        {label}
        {required && <span className="text-rose-700">*</span>}
      </FieldLabel>
      <div className="relative">
        <Input
          type={isVisible ? "text" : "password"}
          value={field.state.value}
          onChange={(e) => field.handleChange(e.target.value)}
          onBlur={field.handleBlur}
          {...props}
        />
        <button
          type="button"
          onClick={toggleVisibility}
          className="absolute top-1/2 -translate-y-1/2 right-2 cursor-pointer"
          aria-label={isVisible ? "Hide password" : "Show password"}
        >
          <HugeiconsIcon icon={isVisible ? Eye : EyeOff} className="size-4" />
        </button>
      </div>
      <FormFieldError errors={errors} />
    </Field>
  );
};
