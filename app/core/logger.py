import logging
import sys

from app.config import get_settings

settings = get_settings()


def init_logging():
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        stream=sys.stdout,
    )


def get_logger(name: str = "app"):
    return logging.getLogger(name)
