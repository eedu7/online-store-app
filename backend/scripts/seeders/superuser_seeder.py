from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import DBRole, DBUser
from core.security.password import get_password_service

password_service = get_password_service()


class SuperuserSeeder:
    ADMIN_ROLE = "admin"

    @staticmethod
    async def create_role(session: AsyncSession) -> DBRole:
        result = await session.execute(
            select(DBRole).where(DBRole.name == SuperuserSeeder.ADMIN_ROLE)
        )
        role = result.scalars().first()

        if role:
            return role
        role = DBRole(
            name=SuperuserSeeder.ADMIN_ROLE, description="System Administrator"
        )
        session.add(role)
        await session.flush()

        return role

    @staticmethod
    async def create_superuser(session: AsyncSession, role: DBRole) -> None:
        result = await session.execute(
            select(DBUser).where(DBUser.email == "admin@example.com")
        )
        user = result.scalars().first()

        if user:
            if role not in user.roles:
                user.roles.append(role)
            return

        user = DBUser(
            username="admin",
            email="admin@example.com",
            password=password_service.hash_password("admin"),
            email_verified=True,
            first_name="System",
            last_name="Admin",
        )
        user.roles.append(role)

        session.add(user)

    @staticmethod
    async def run(session: AsyncSession) -> None:
        role = await SuperuserSeeder.create_role(session)

        await SuperuserSeeder.create_superuser(session=session, role=role)
