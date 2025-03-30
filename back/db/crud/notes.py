from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, select
from db.models.notes import Note

from datetime import datetime as dt


async def get_notes(
        student_id: int,
        session: AsyncSession
) -> list[Note]:
    async with session:
        stmt = select(Note).where(Note.student_id == student_id)
        res = await session.execute(stmt)

        return res.scalars().all()


async def add_note(
        title: str,
        content: str,
        student_id: int,
        teacher_id: int,
        deadline: dt,
        session: AsyncSession
) -> Note:
    async with session:
        note = Note(
            title=title,
            content=content,
            student_id=student_id,
            teacher_id=teacher_id,
            deadline=deadline.replace(tzinfo=None),
        )
        session.add(note)
        await session.commit()
        await session.refresh(note)

        return note


async def update_note(
        note_id: int,
        title: str,
        content: str,
        student_id: int,
        teacher_id: int,
        deadline: dt,
        done: bool,
        session: AsyncSession
) -> Note:
    async with session:
        stmt = (
            update(Note)
            .where(Note.id == note_id)
            .values(
                title=title,
                content=content,
                student_id=student_id,
                teacher_id=teacher_id,
                deadline=deadline,
                done=done
            ).returning(Note)
        )
        res = await session.execute(stmt)
        await session.commit()

        return res.scalar_one()
