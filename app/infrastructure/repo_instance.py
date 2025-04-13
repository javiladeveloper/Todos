from app.config import get_settings
from app.infrastructure.in_memory_repo import InMemoryTaskRepository
from app.infrastructure.interfaces import AbstractTaskRepository

_repo_instance: AbstractTaskRepository | None = None


def get_repository() -> AbstractTaskRepository:
    global _repo_instance

    if _repo_instance is None:
        settings = get_settings()

        if settings.repo_type == "memory":
            _repo_instance = InMemoryTaskRepository()
        elif settings.repo_type == "mongo":
            raise NotImplementedError("Mongo repository not implemented yet.")
        elif settings.repo_type == "athena":
            raise NotImplementedError("Athena repository not implemented yet.")
        else:
            raise ValueError(f"Unsupported repo_type: {settings.repo_type}")

    return _repo_instance
