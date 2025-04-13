from abc import ABC, abstractmethod
from typing import List

from app.domain.entities import Task


class AbstractTaskRepository(ABC):
    @abstractmethod
    def list_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    def get_task(self, task_id: int) -> Task:
        pass

    @abstractmethod
    def create_task(self, task: Task) -> Task:
        pass

    @abstractmethod
    def update_task(self, task_id: int, task: Task) -> Task:
        pass

    @abstractmethod
    def delete_task(self, task_id: int) -> None:
        pass
