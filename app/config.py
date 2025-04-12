import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv(".env")

env_name = os.getenv("ENV", "dev")

dotenv_path = Path(f".env.{env_name}")
load_dotenv(dotenv_path, override=True)


class Settings(BaseSettings):
    env: str = env_name
    api_version_path: str = "v1"
    log_level: str
    enable_graphql: bool
    lang: str = os.getenv("LANG", "es")
    api_title: str
    api_version: str
    api_description: str
    api_contact_name: str
    api_contact_url: str
    api_contact_email: str

    class Config:
        env_file = dotenv_path


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
