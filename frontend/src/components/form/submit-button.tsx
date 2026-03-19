import { useFormContext } from "@/context/form";
import { Button } from "@/components/ui/button";

export const SubmitButton = ({
  label,
}: {
  label: string;
}): React.JSX.Element => {
  const form = useFormContext();
  return (
    <form.Subscribe selector={(state) => state.isSubmitting}>
      {(isSubmitting) => (
        <Button type="submit" disabled={isSubmitting}>
          {label}
        </Button>
      )}
    </form.Subscribe>
  );
};
