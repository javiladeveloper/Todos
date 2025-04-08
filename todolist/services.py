from typing import List
from todolist import storage
from todolist.schemas import Task, TaskCreate, TaskUpdate
from todolist.exceptions import TASK_NOT_FOUND
import logging

logger = logging.getLogger(__name__)


def list_tasks() -> List[Task]:
    return storage.get_all()


def get_task(task_id: int) -> Task:
    task = storage.get(task_id)
    if not task:
        logger.warning(f"Tarea con ID {task_id} no encontrada.")
        raise TASK_NOT_FOUND
    return task


def create_task(data: TaskCreate) -> Task:
    return storage.create(data.dict())


def update_task(task_id: int, data: TaskUpdate) -> Task:
    task = storage.update(task_id, data.dict())
    if not task:
        logger.warning(f"Intento de actualizar tarea inexistente con ID {task_id}")
        raise TASK_NOT_FOUND
    return task


def delete_task(task_id: int) -> None:
    success = storage.delete(task_id)
    if not success:
        logger.warning(f"Intento de eliminar tarea inexistente con ID {task_id}")
        raise TASK_NOT_FOUND
