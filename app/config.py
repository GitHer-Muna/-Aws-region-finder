from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AWS Region Finder"
    class Config:
        env_file = ".env"

settings = Settings()
