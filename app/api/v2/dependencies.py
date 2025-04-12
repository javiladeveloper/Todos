from fastapi import Depends

from app.infrastructure.interfaces import TaskRepository
from app.infrastructure.repo_instance import repo_instance
from app.services.task_service import TaskService


def get_task_repo() -> TaskRepository:
    return repo_instance


def get_task_service(repo: TaskRepository = Depends(get_task_repo)) -> TaskService:
    return TaskService(repo)
