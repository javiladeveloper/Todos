import os
import sys
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv(".env")

env_name = os.getenv("ENV", "dev")
dotenv_path = Path(f".env.{env_name}")
load_dotenv(dotenv_path, override=True)


def is_testing():
    return "pytest" in sys.argv[0] or os.getenv("PYTEST_CURRENT_TEST") is not None


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
    if is_testing():
        return Settings(
            log_level="INFO",
            enable_graphql=True,
            lang="es",
            api_title="Mock API",
            api_version="1.0.0",
            api_description="Mocked description",
            api_contact_name="Test User",
            api_contact_url="http://localhost",
            api_contact_email="test@example.com",
        )
    return Settings()
