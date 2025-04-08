from typing import List, Optional

from todolist.schemas import Task


class TaskStorage:
    def __init__(self):
        self.tasks: List[Task] = []
        self.counter = 1

    def get_all(self) -> List[Task]:
        return self.tasks

    def get(self, task_id: int) -> Optional[Task]:
        return next((task for task in self.tasks if task.id == task_id), None)

    def create(self, task_data: dict) -> Task:
        task = Task(id=self.counter, **task_data)
        self.tasks.append(task)
        self.counter += 1
        return task

    def update(self, task_id: int, task_data: dict) -> Optional[Task]:
        task = self.get(task_id)
        if task:
            task.title = task_data["title"]
            task.description = task_data.get("description", "")
            task.completed = task_data["completed"]
            return task
        return None

    def delete(self, task_id: int) -> bool:
        task = self.get(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False


storage = TaskStorage()
