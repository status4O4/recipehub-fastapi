from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI App"
    DEBUG: bool = False

    DB_URL: str

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    LOG_LEVEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[arg-type]
