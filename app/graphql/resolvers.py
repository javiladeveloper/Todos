from typing import Optional

import strawberry

from app.core.exceptions import InvalidTaskData
from app.graphql.types import PaginatedTaskType, TaskInput, TaskType, TaskUpdateInput
from app.infrastructure.repo_instance import repo_instance
from app.services.task_service import TaskService

service = TaskService(repo_instance)


@strawberry.type
class Query:
    @strawberry.field
    def tasks(self, page: int = 1, page_size: int = 10) -> PaginatedTaskType:
        offset = (page - 1) * page_size
        items = [
            TaskType(**task.__dict__)
            for task in service.list_tasks(limit=page_size, offset=offset)
        ]
        total = service.total_tasks()
        total_pages = (total + page_size - 1) // page_size

        return PaginatedTaskType(
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
            items=items,
        )

    @strawberry.field
    def task(self, id: int) -> Optional[TaskType]:
        try:
            task = service.get_task(id)
            return TaskType(**task.__dict__)
        except Exception:
            return None


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_task(self, input: TaskInput) -> TaskType:
        if not input.title.strip():
            raise InvalidTaskData("El título no puede estar vacío.")
        if input.completed and not input.description.strip():
            raise InvalidTaskData("Las tareas completadas deben tener una descripción.")

        created = service.create_task(input.__dict__)
        return TaskType(**created.__dict__)

    @strawberry.mutation
    def update_task(self, id: int, input: TaskUpdateInput) -> TaskType:
        if not input.title.strip():
            raise InvalidTaskData("El título no puede estar vacío.")
        if input.completed and not input.description.strip():
            raise InvalidTaskData("Las tareas completadas deben tener una descripción.")

        updated = service.update_task(id, input.__dict__)
        return TaskType(**updated.__dict__)

    @strawberry.mutation
    def delete_task(self, id: int) -> bool:
        return service.delete_task(id)
