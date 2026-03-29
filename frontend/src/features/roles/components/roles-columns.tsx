"use client";

import {
  CopyFreeIcons,
  Delete01FreeIcons,
  Edit02FreeIcons,
  MoreHorizontalSquare01FreeIcons,
} from "@hugeicons/core-free-icons";
import {HugeiconsIcon} from "@hugeicons/react";
import type {ColumnDef} from "@tanstack/react-table";
import {Button} from "@/components/ui/button";
import {Checkbox} from "@/components/ui/checkbox";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import type {Role} from "@/features/roles/roles.types";
import {formatDate} from "@/lib/utils";

export const RoleColumns: ColumnDef<Role>[] = [
  {
    cell: ({ row }) => (
      <Checkbox
        aria-label="Select row"
        checked={row.getIsSelected()}
        onCheckedChange={(value) => row.toggleSelected(value)}
      />
    ),
    enableHiding: false,
    enableSorting: false,
    header: ({ table }) => (
      <Checkbox
        aria-label="Select all"
        checked={table.getIsAllPageRowsSelected()}
        onCheckedChange={(value) => table.toggleAllPageRowsSelected(value)}
      />
    ),
    id: "select",
  },
  {
    accessorKey: "name",
    header: "Role",
  },
  {
    accessorKey: "description",
    header: "Description",
  },
  {
    accessorKey: "created_at",
    cell: ({ row }) => formatDate(row.original.created_at),
    header: "Created",
  },
  {
    accessorKey: "updated_at",
    cell: ({ row }) => formatDate(row.original.updated_at),
    header: "Updated",
  },
  {
    cell: ({ row }) => {
      const role = row.original;
      return (
        <DropdownMenu>
          <DropdownMenuTrigger
            render={
              <Button className="size-8 p-0" variant="ghost">
                <span className="sr-only">Open menu</span>
                <HugeiconsIcon icon={MoreHorizontalSquare01FreeIcons} />
              </Button>
            }
          />
          <DropdownMenuGroup>
            <DropdownMenuContent align="end">
              <DropdownMenuItem
                onClick={() => navigator.clipboard.writeText(role.id)}
              >
                <HugeiconsIcon icon={CopyFreeIcons} />
                Copy role ID
              </DropdownMenuItem>
              <DropdownMenuItem>
                <HugeiconsIcon icon={Edit02FreeIcons} />
                Edit
              </DropdownMenuItem>
              <DropdownMenuItem variant="destructive">
                <HugeiconsIcon icon={Delete01FreeIcons} />
                Delete
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenuGroup>
        </DropdownMenu>
      );
    },
    id: "actions",
  },
];
