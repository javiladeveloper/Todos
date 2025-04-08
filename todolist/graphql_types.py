from typing import List, Optional

import strawberry

from todolist import services


@strawberry.type
class TaskType:
    id: int
    title: str
    description: str
    completed: bool


@strawberry.type
class Query:
    tasks: List[TaskType] = strawberry.field(resolver=lambda: services.list_tasks())

    @strawberry.field
    def task(self, id: int) -> Optional[TaskType]:
        return services.get_task(id)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_task(
        self, title: str, description: str = "", completed: bool = False
    ) -> TaskType:
        from todolist.schemas import TaskCreate

        data = TaskCreate(title=title, description=description, completed=completed)
        return services.create_task(data)

    @strawberry.mutation
    def update_task(
        self, id: int, title: str, description: str = "", completed: bool = False
    ) -> TaskType:
        from todolist.schemas import TaskUpdate

        data = TaskUpdate(title=title, description=description, completed=completed)
        return services.update_task(id, data)

    @strawberry.mutation
    def delete_task(self, id: int) -> bool:
        services.delete_task(id)
        return True
