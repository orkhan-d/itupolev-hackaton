from sqlalchemy.orm import Mapped, mapped_column
from db.base import Base


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)

    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    token: Mapped[str | None] = mapped_column()