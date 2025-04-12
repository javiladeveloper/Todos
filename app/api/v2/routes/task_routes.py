from fastapi import APIRouter, Depends, Path, Query, status

from app.api.v1.dependencies import get_task_service
from app.core.exceptions import PageOutOfRange
from app.domain.schemas import PaginatedTasks, TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter()


@router.get(
    "/", response_model=PaginatedTasks, summary="Listar tareas", tags=["Tareas"]
)
def list_tasks(
    page: int = Query(1, ge=1, alias="page", description="Número de página"),
    page_size: int = Query(
        10, ge=1, le=100, alias="page_size", description="Elementos por página"
    ),
    service: TaskService = Depends(get_task_service),
):
    offset = (page - 1) * page_size
    tasks = service.list_tasks(limit=page_size, offset=offset)
    total = service.total_tasks()
    total_pages = (total + page_size - 1) // page_size
    if page > total_pages and total > 0:
        raise PageOutOfRange()

    return {
        "items": tasks,
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
    }


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
    summary="Obtener tarea por ID",
    tags=["Tareas"],
)
def get_task(
    task_id: int = Path(..., ge=1),
    service: TaskService = Depends(get_task_service),
):
    return service.get_task(task_id)


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear tarea",
    tags=["Tareas"],
)
def create_task(
    task: TaskCreate,
    service: TaskService = Depends(get_task_service),
):
    return service.create_task(task.dict())


@router.put(
    "/{task_id}",
    response_model=TaskResponse,
    summary="Actualizar tarea por ID",
    tags=["Tareas"],
)
def update_task(
    task_id: int = Path(..., ge=1),
    task: TaskUpdate = ...,
    service: TaskService = Depends(get_task_service),
):
    return service.update_task(task_id, task.dict())


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar tarea",
    tags=["Tareas"],
)
def delete_task(
    task_id: int = Path(..., ge=1),
    service: TaskService = Depends(get_task_service),
):
    service.delete_task(task_id)
