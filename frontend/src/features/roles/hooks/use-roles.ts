import { useQuery } from "@tanstack/react-query";
import type { Role } from "@/features/roles/roles.types";
import { apiBrowserClient } from "@/lib/api/api.client";

const useCreateRole = () => {};
const useGetRoles = () =>
  useQuery({
    queryFn: async (): Promise<Role[]> => {
      return await apiBrowserClient("/roles", {
        method: "GET",
      });
    },
    queryKey: ["roles", "use-roles"],
  });
const useGetRoleById = () => {};
const useUpdateRole = () => {};
const useDeleteRole = () => {};

export {
  useCreateRole,
  useDeleteRole,
  useGetRoleById,
  useGetRoles,
  useUpdateRole,
};
