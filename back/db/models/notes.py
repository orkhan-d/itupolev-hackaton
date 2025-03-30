from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base
from db.models.teachers import Teacher

from datetime import datetime as dt


class Note(Base):
    __tablename__ = 'notes'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()

    student_id: Mapped[int] = mapped_column(ForeignKey('notes.id'))

    teacher_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'))
    teacher: Mapped["Teacher"] = relationship("Teacher", lazy="selectin")

    done: Mapped[bool] = mapped_column(server_default='false')
    deadline: Mapped[dt] = mapped_column()
