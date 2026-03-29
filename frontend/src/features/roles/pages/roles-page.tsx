"use client";
import { RoleColumns } from "@/features/roles/components/roles-columns";
import { RoleDataTable } from "@/features/roles/components/roles-data-table";
import { useGetRoles } from "@/features/roles/hooks/use-roles";

export const RolesPage = () => {
  const { data } = useGetRoles();
  return (
    <div className="p-12">
      <RoleDataTable columns={RoleColumns} data={data || []} />
    </div>
  );
};
