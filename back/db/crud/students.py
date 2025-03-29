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


async def add_student_token(student_id: int,
                            session: AsyncSession) -> str:
    async with session:
        token = str(uuid4())
        stmt = (update(Student)
                .where(Student.id == student_id)
                .values(token=token)
                .returning(Student.token))

        res = await session.execute(stmt)
        await session.commit()

        return res.scalar_one()