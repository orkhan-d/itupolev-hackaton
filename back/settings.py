from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    USER: str
    PASS: str
    HOST: str
    PORT: int
    NAME: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "DATABASE_"
        extra = "ignore"


class Settings(BaseSettings):
    DATABASE: DatabaseConfig = DatabaseConfig()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
