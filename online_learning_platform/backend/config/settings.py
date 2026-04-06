from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application configuration using environment variables."""

    app_name: str = "Online Learning Platform"
    database_url: str = "sqlite:///./dev.db"
    secret_key: str = "supersecret"

    class Config:
        env_file = ".env"

settings = Settings()
