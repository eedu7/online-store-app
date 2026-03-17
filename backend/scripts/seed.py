import asyncio

from core.database.session import AsyncSessionLocal
from scripts.seeders.superuser_seeder import SuperuserSeeder


async def main():

    async with AsyncSessionLocal() as session:
        await SuperuserSeeder.run(session)

        await session.commit()


if __name__ == "__main__":
    asyncio.run(main())
