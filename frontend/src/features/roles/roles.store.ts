import { create } from "zustand";
import type { Role } from "@/features/roles/roles.types";

type Modal = "create" | "edit" | "delete" | null;

interface RoleStore {
  open: Modal;
  setOpen: (modal: Modal) => void;
  role: Role | null;
  setRole: (role: Role) => void;
  clearRole: () => void;
}

export const useRoleStore = create<RoleStore>((set) => ({
  clearRole: () => set({ role: null }),
  open: null,
  role: null,
  setOpen: (modal) => set({ open: modal }),
  setRole: (role) => set({ role }),
}));
