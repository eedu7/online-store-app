"use client";

import { useFieldContext } from "@/context/form";
import { useStore } from "@tanstack/react-form";
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { InputHTMLAttributes, useState } from "react";
import { HugeiconsIcon } from "@hugeicons/react";
import { Eye, EyeOff } from "@hugeicons/core-free-icons";

interface Props extends InputHTMLAttributes<HTMLInputElement> {
  label: string;
}

export const PasswordField = ({
  label,
  ...props
}: Props): React.JSX.Element => {
  const field = useFieldContext<string>();

  const errors = useStore(field.store, (state) => state.meta.errors);
  const [isVisible, setIsVisible] = useState<boolean>(false);
  const toggleVisibility = () => setIsVisible((prev) => !prev);
  return (
    <Field>
      <FieldLabel>{label}</FieldLabel>
      <div className="relative">
        <Input
          type={isVisible ? "text" : "password"}
          value={field.state.value}
          onChange={(e) => field.handleChange(e.target.value)}
          onBlur={field.handleBlur}
          {...props}
        />
        <HugeiconsIcon
          icon={isVisible ? Eye : EyeOff}
          onClick={toggleVisibility}
          className="absolute top-1/2 -translate-y-1/2 right-2 size-4 cursor-pointer"
        />
      </div>
      {errors.map((error: string) => (
        <FieldDescription key={error} className="text-rose-500">
          {error}
        </FieldDescription>
      ))}
    </Field>
  );
};
