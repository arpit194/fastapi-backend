from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    BACKEND_VER: str
    DOCS_URL: str
    REDOC_URL: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )


def get_app_settings():
    return AppSettings()
