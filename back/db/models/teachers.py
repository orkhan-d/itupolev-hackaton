from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    id: Mapped[int] = mapped_column(primary_key=True)

    surname: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()

    type_id: Mapped[int] = mapped_column(ForeignKey('teacher_types.id'))
    type: Mapped["TeacherType"] = relationship("TeacherType", lazy="selectin")


class TeacherType(Base):
    __tablename__ = 'teacher_types'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()