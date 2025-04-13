from fastapi import Depends

from app.infrastructure.interfaces import AbstractTaskRepository
from app.infrastructure.repo_instance import get_repository
from app.services.task_service import TaskService


def get_task_repo() -> AbstractTaskRepository:
    return get_repository()


def get_task_service(
    repo: AbstractTaskRepository = Depends(get_task_repo),
) -> TaskService:
    return TaskService(repo)
