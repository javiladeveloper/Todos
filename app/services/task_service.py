from typing import Dict, List

from app.core.exceptions import InvalidTaskData, TaskNotFoundError
from app.core.logger import get_logger
from app.domain.entities import Task
from app.infrastructure.interfaces import AbstractTaskRepository

logger = get_logger(__name__)


class TaskService:
    def __init__(self, repo: AbstractTaskRepository) -> None:
        self.repo: AbstractTaskRepository = repo

    def list_tasks(self, limit: int = 10, offset: int = 0) -> List[Task]:
        logger.info(
            "Listando tareas con paginación: limit=%s, offset=%s", limit, offset
        )
        all_tasks = self.repo.list_tasks()
        return all_tasks[offset : offset + limit]

    def get_task(self, task_id: int) -> Task:
        task: Task | None = self.repo.get_task(task_id)
        if not task:
            logger.warning(f"Tarea con ID {task_id} no encontrada")
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        return task

    def create_task(self, data: Dict) -> Task:
        logger.debug("Datos recibidos para creación: %s", data)
        self._validate_task_data(data)
        logger.info(f"Creando tarea: {data}")
        return self.repo.create_task(Task(**data))

    def update_task(self, task_id: int, data: Dict) -> Task:
        logger.debug("Actualizando tarea %s con datos: %s", task_id, data)
        self._validate_task_data(data)
        task = self.repo.update_task(task_id, Task(id=task_id, **data))
        if not task:
            logger.warning(f"Intento de actualizar tarea inexistente ID {task_id}")
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        logger.info(f"Tarea actualizada: {task}")
        return task

    def delete_task(self, task_id: int) -> bool:
        logger.debug("Eliminando tarea con ID: %s", task_id)
        deleted: bool = self.repo.delete_task(task_id)
        if not deleted:
            logger.warning(f"Intento de eliminar tarea inexistente ID {task_id}")
            raise TaskNotFoundError(f"Task with ID {task_id} not found")
        logger.info(f"Tarea eliminada ID {task_id}")
        return True

    def total_tasks(self) -> int:
        return len(self.repo.list_tasks())

    def _validate_task_data(self, data: Dict) -> None:
        title = data.get("title", "").strip()
        description = data.get("description", "").strip()
        completed = data.get("completed", False)

        if not title:
            raise InvalidTaskData("El título no puede estar vacío.")
        if completed and not description:
            raise InvalidTaskData("Las tareas completadas deben tener una descripción.")
