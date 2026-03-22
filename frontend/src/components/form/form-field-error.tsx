import { FieldError } from "@/components/ui/field";

interface FieldErrorsProps {
  errors: any[];
}

export const FormFieldError = ({
  errors,
}: FieldErrorsProps): React.JSX.Element | null => {
  if (!errors.length) return null;
  return (
    <div>
      {errors.map((error: any) => (
        <FieldError key={error} className="text-rose-700">
          {error?.message}
        </FieldError>
      ))}
    </div>
  );
};
