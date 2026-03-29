"use client";
import { CreateEditRoleModal } from "@/features/roles/components/create-edit-role-modal";
import { RemoveRoleModal } from "@/features/roles/components/remove-role-modal";
import { RoleColumns } from "@/features/roles/components/roles-columns";
import { RoleDataTable } from "@/features/roles/components/roles-data-table";
import { useGetRoles } from "@/features/roles/hooks/use-roles";

export const RolesPage = () => {
  const { data } = useGetRoles();
  return (
    <>
      <div className="p-12">
        <RoleDataTable columns={RoleColumns} data={data || []} />
      </div>
      <CreateEditRoleModal />
      <RemoveRoleModal />
    </>
  );
};
