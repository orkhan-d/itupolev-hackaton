from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base

if TYPE_CHECKING:
    from db.models.subjects import Subject
    from db.models.teachers import Teacher
    from db.models.classes import Class


class Timetable(Base):
    __tablename__ = 'timetables'

    id: Mapped[int] = mapped_column(primary_key=True)

    day_of_week: Mapped[int] = mapped_column()
    lesson_number: Mapped[int] = mapped_column()

    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    class_: Mapped["Class"] = relationship("Class", lazy="selectin")

    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    taecher: Mapped["Teacher"] = relationship("Teacher", lazy="selectin")

    subject_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    subject: Mapped["Subject"] = relationship("Subject", lazy="selectin")