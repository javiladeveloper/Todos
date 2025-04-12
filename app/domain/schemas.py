from typing import List

from pydantic import BaseModel, Field, root_validator, validator

from app.core.exceptions import InvalidTaskData


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(default="", max_length=300)
    completed: bool = False

    @validator("title")
    def no_empty_titles(cls, v):
        if not v.strip():
            raise InvalidTaskData("El título no puede estar vacío")
        return v

    @root_validator
    def description_required_if_completed(cls, values):
        completed = values.get("completed")
        description = values.get("description", "").strip()
        if completed and not description:
            raise InvalidTaskData("Las tareas completadas deben tener una descripción")
        return values


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int


class PaginatedTasks(BaseModel):
    total: int
    page: int
    page_size: int
    total_pages: int
    items: List[TaskResponse]
