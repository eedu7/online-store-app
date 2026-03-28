import {useQuery} from "@tanstack/react-query";
import type {Role} from "@/features/roles/roles.types";
import {apiServerClient} from "@/lib/api/api.server";

const createRole = () => {};
const getRoles = () =>
  useQuery({
    queryFn: async (): Promise<Role[]> => {
      return await apiServerClient("/roles", {
        method: "GET",
      });
    },
    queryKey: ["roles", "use-roles"],
  });
const getRoleById = () => {};
const updateRole = () => {};
const deleteRole = () => {};

export { createRole, deleteRole, getRoleById, getRoles, updateRole };
