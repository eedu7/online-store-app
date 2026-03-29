import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { useRoleStore } from "@/features/roles/roles.store";

export const CreateEditRoleModal = () => {
  const { open, role, clearRole } = useRoleStore();

  const createModal = open === "create";
  const editModal = open === "edit" && role;

  if (!createModal && !editModal) return null;

  return (
    <Dialog onOpenChange={clearRole} open={true}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>{createModal ? "Create Role" : "Edit Role"}</DialogTitle>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  );
};
