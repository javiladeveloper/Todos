from typing import List

from fastapi import APIRouter

from todolist import services
from todolist.schemas import Task, TaskCreate, TaskUpdate

router = APIRouter()


@router.get("/tasks/", response_model=List[Task])
def get_tasks():
    return services.list_tasks()


@router.post("/tasks/", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    return services.create_task(task)


@router.get("/tasks/{task_id}/", response_model=Task)
def read_task(task_id: int):
    return services.get_task(task_id)


@router.put("/tasks/{task_id}/", response_model=Task)
def update_task(task_id: int, task: TaskUpdate):
    return services.update_task(task_id, task)


@router.delete("/tasks/{task_id}/", status_code=204)
def delete_task(task_id: int):
    services.delete_task(task_id)
