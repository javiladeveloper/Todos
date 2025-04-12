from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities import Task


class TaskRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Task]: ...

    @abstractmethod
    def get(self, task_id: int) -> Optional[Task]: ...

    @abstractmethod
    def create(self, data: dict) -> Task: ...

    @abstractmethod
    def update(self, task_id: int, data: dict) -> Optional[Task]: ...

    @abstractmethod
    def delete(self, task_id: int) -> bool: ...
