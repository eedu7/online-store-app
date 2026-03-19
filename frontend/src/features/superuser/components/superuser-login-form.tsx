import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSet,
} from "@/components/ui/field";
import { Input } from "@/components/ui/input";

export const SuperuserLoginForm = () => {
  return (
    <form>
      <FieldGroup>
        <FieldSet>
          <FieldLegend>Login Title</FieldLegend>
          <FieldDescription>Login Description</FieldDescription>
          <FieldGroup>
            <Field>
              <FieldLabel>Username or Email</FieldLabel>
              <Input />
            </Field>
            <Field>
              <FieldLabel>Password</FieldLabel>
              <Input />
            </Field>
          </FieldGroup>
        </FieldSet>
      </FieldGroup>
    </form>
  );
};
