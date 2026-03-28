import {SidebarInset, SidebarProvider} from "@/components/ui/sidebar";
import {ReactNode} from "react";
import {AdminSidebar} from "@/features/admin/components/admin-sidebar";

export const AdminLayout = ({children}: {children: ReactNode}) => {
    return (
        <SidebarProvider

        >
            <AdminSidebar/>
            <SidebarInset>
                {children}
            </SidebarInset>
        </SidebarProvider>
    )
}