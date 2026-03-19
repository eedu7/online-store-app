import { PasswordField } from "@/components/form/password-field";
import { TextField } from "@/components/form/text-field";
import { SubmitButton } from "@/components/form/submit-button";
import { createFormHook, createFormHookContexts } from "@tanstack/react-form";

const { fieldContext, formContext } = createFormHookContexts();

export const { useAppForm } = createFormHook({
  fieldComponents: {
    TextField,
    PasswordField,
  },
  formComponents: {
    SubmitButton,
  },
  fieldContext,
  formContext,
});
