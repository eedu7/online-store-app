"use state";
import { useFieldContext } from "@/hooks/form-context";
import { useStore } from "@tanstack/react-form";
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field";
import { Input } from "@/components/ui/input";

export const TextField = ({ label }: { label: string }) => {
  const field = useFieldContext<string>();

  const errors = useStore(field.store, (state) => state.meta.errors);

  return (
    <Field>
      <FieldLabel>{label}</FieldLabel>
      <Input
        value={field.state.value}
        onChange={(e) => field.handleChange(e.target.value)}
        onBlur={field.handleBlur}
      />
      {errors.map((error: string) => (
        <FieldDescription key={error} className="text-rose-500">
          {error}
        </FieldDescription>
      ))}
    </Field>
  );
};
