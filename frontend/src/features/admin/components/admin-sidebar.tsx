import {
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarTrigger
} from "@/components/ui/sidebar";
import Link from "next/link";
import {HugeiconsIcon} from "@hugeicons/react";
import {Users} from "@hugeicons/core-free-icons";

export const AdminSidebar = () => {
    return (
        <Sidebar
        collapsible="icon"
        >
            <SidebarHeader>
                <SidebarMenu>
                    <SidebarMenuItem>
                        <SidebarTrigger/>
                    </SidebarMenuItem>
                </SidebarMenu>
            </SidebarHeader>
            <SidebarContent>
                <SidebarGroup>
                    <SidebarGroupContent>
                        <SidebarMenu>
                            <SidebarMenuItem
                            >
                                <SidebarMenuButton
                                    tooltip="Roles"
                                render={
                                    <Link href="/dashboard/roles">
                                        <HugeiconsIcon
icon={Users}
                                        />
                                        <span>Roles</span>
                                    </Link>
                                }
                                />

                            </SidebarMenuItem>
                        </SidebarMenu>
                    </SidebarGroupContent>
                </SidebarGroup>
            </SidebarContent>
        </Sidebar>
    )
}