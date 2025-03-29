from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncAttrs
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from settings import settings

DATABASE_USER = settings.DATABASE.USER
DATABASE_PASS = settings.DATABASE.PASS
DATABASE_HOST = settings.DATABASE.HOST
DATABASE_PORT = settings.DATABASE.PORT
DATABASE_NAME = settings.DATABASE.NAME

DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{DATABASE_USER}:{DATABASE_PASS}@"
    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)
engine = create_async_engine(DATABASE_URL, echo=True)
session_pool = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    pass
