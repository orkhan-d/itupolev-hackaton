from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base
from db.models.classes import Class


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)

    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()

    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    class_: Mapped["Class"] = relationship("Class", lazy="selectin")
