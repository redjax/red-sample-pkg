from pydantic import Field, field_validator, ValidationError
from pydantic_settings import BaseSettings

from config import settings, database_settings


class AppSettings(BaseSettings):
    env: str = Field(default=settings.ENV, env="ENV")
    container_env: bool = Field(default=settings.CONTAINER_ENV, env="CONTAINER_ENV")
    log_level: str = Field(default=settings.LOG_LEVEL, env="LOG_LEVEL")


class DBSettings(BaseSettings):
    type: str = Field(default=database_settings.TYPE, env="DB_TYPE")
    host: str = Field(default=database_settings.HOST, env="DB_HOST")
