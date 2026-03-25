export default async function Layout({
  admin,
  tenant,
}: Readonly<{ admin: React.ReactNode; tenant: React.ReactNode }>) {
  return tenant;
}
