from sqlalchemy.orm import Mapped, mapped_column
from db.base import Base


class Subject(Base):
    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
