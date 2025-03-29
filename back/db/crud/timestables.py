from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.timetable import Timetable

#Рассписание 
async def get_class_timetable( # РАссписание группы 
        class_id: int,
        session: AsyncSession
) -> list[Timetable]:
    async with session:
        stmt = (select(Timetable)
                .where(Timetable.class_id == class_id)
                .order_by(Timetable.day_of_week)
                .order_by(Timetable.lesson_number))
        res = await session.execute(stmt)

        return res.scalars().all()


async def get_teacher_timetable(teacher_id: int,  #Рассписание отдельного препода 
                                session: AsyncSession) -> str:
    async with session:
        stmt = (select(Timetable)
                .where(Timetable.teacher_id == teacher_id)
                .order_by(Timetable.day_of_week)
                .order_by(Timetable.lesson_number))

        res = await session.execute(stmt)
        return res.scalars().all()
