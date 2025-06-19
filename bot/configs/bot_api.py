from pydantic import  Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str = Field(..., env="BOT_TOKEN")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow"
    )

config = Settings()