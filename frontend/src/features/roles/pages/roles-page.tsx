import { RoleColumns } from "@/features/roles/components/roles-columns";
import { RoleDataTable } from "@/features/roles/components/roles-data-table";
import type { Role } from "@/features/roles/roles.types";

const data: Role[] = [
  {
    created_at: "2022-07-15",
    description: "Full access to all system features and settings",
    id: "01",
    name: "Admin",
    updated_at: "2024-05-12",
  },
  {
    created_at: "2022-08-10",
    description: "Can manage teams, projects, and view reports",
    id: "02",
    name: "Manager",
    updated_at: "2024-03-22",
  },
  {
    created_at: "2022-09-05",
    description: "Can create and edit content but cannot manage users",
    id: "03",
    name: "Editor",
    updated_at: "2024-02-18",
  },
  {
    created_at: "2022-10-01",
    description: "Read-only access to view content and reports",
    id: "04",
    name: "Viewer",
    updated_at: "2024-01-10",
  },
  {
    created_at: "2023-01-12",
    description: "Handles customer queries and support tickets",
    id: "05",
    name: "Support",
    updated_at: "2024-04-02",
  },
  {
    created_at: "2023-03-20",
    description: "Limited access for temporary or external users",
    id: "06",
    name: "Guest",
    updated_at: "2023-12-15",
  },
];

export const RolesPage = () => {
  return (
    <div className="p-12">
      <RoleDataTable columns={RoleColumns} data={data} />
    </div>
  );
};
