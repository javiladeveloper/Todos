from typing import List

import strawberry


@strawberry.type
class TaskType:
    id: int
    title: str
    description: str
    completed: bool


@strawberry.input
class TaskInput:
    title: str
    description: str = ""
    completed: bool = False


@strawberry.input
class TaskUpdateInput:
    title: str
    description: str
    completed: bool


@strawberry.type
class PaginatedTaskType:
    total: int
    page: int
    page_size: int
    total_pages: int
    items: List[TaskType]
