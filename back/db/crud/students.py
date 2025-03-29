from uuid import uuid4

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from db.models.students import Student


async def get_user_by_credentials(
        login: str,
        password: str,
        session: AsyncSession
) -> Student | None:
    async with session:
        stmt = (select(Student)
                .where(Student.login == login)
                .where(Student.password == password))
        res = await session.execute(stmt)

        return res.scalar_one_or_none()
