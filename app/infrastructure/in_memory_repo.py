from typing import List

from app.core.exceptions import TaskNotFoundError
from app.domain.entities import Task
from app.infrastructure.interfaces import AbstractTaskRepository


class InMemoryTaskRepository(AbstractTaskRepository):
    def __init__(self):
        self.tasks: List[Task] = []
        self.counter = 1

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def get_task(self, task_id: int) -> Task:
        task = next((t for t in self.tasks if t.id == task_id), None)
        if not task:
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        return task

    def create_task(self, task: Task) -> Task:
        task.id = self.counter
        self.tasks.append(task)
        self.counter += 1
        return task

    def update_task(self, task_id: int, updated_task: Task) -> Task:
        task = self.get_task(task_id)
        task.title = updated_task.title
        task.description = updated_task.description
        task.completed = updated_task.completed
        return task

    def delete_task(self, task_id: int) -> bool:
        try:
            task = self.get_task(task_id)
            self.tasks.remove(task)
            return True
        except TaskNotFoundError:
            return False
