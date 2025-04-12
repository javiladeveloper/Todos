from typing import List, Optional

from app.domain.entities import Task
from app.infrastructure.interfaces import TaskRepository


class InMemoryTaskRepo(TaskRepository):
    def __init__(self):
        self.tasks: List[Task] = []
        self.counter = 1

    def get_all(self) -> List[Task]:
        return self.tasks

    def get(self, task_id: int) -> Optional[Task]:
        return next((t for t in self.tasks if t.id == task_id), None)

    def create(self, data: dict) -> Task:
        task = Task(id=self.counter, **data)
        self.tasks.append(task)
        self.counter += 1
        return task

    def update(self, task_id: int, data: dict) -> Optional[Task]:
        task = self.get(task_id)
        if task:
            task.title = data["title"]
            task.description = data.get("description", "")
            task.completed = data["completed"]
            return task
        return None

    def delete(self, task_id: int) -> bool:
        task = self.get(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
