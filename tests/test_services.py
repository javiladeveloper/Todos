import pytest

from app.core.exceptions import TaskNotFoundError
from app.infrastructure.in_memory_repo import InMemoryTaskRepo
from app.services.task_service import TaskService


@pytest.fixture
def service():
    repo = InMemoryTaskRepo()
    return TaskService(repo)


def test_create_task(service):
    task_data = {"title": "Test", "description": "desc", "completed": False}
    task = service.create_task(task_data)
    assert task.id == 1
    assert task.title == "Test"


def test_list_tasks(service):
    service.create_task({"title": "Task 1", "description": "", "completed": False})
    service.create_task({"title": "Task 2", "description": "", "completed": False})
    tasks = service.list_tasks(limit=10)
    assert len(tasks) == 2


def test_get_task_success(service):
    created = service.create_task(
        {"title": "Get", "description": "", "completed": False}
    )
    task = service.get_task(created.id)
    assert task.id == created.id


def test_get_task_not_found(service):
    with pytest.raises(TaskNotFoundError):
        service.get_task(999)


def test_update_task(service):
    created = service.create_task(
        {"title": "Old", "description": "", "completed": False}
    )
    updated = service.update_task(
        created.id, {"title": "New", "description": "updated", "completed": True}
    )
    assert updated.title == "New"
    assert updated.completed is True


def test_update_task_not_found(service):
    with pytest.raises(TaskNotFoundError):
        service.update_task(999, {"title": "X", "description": "", "completed": False})


def test_delete_task_success(service):
    created = service.create_task(
        {"title": "Delete", "description": "", "completed": False}
    )
    result = service.delete_task(created.id)
    assert result is True


def test_delete_task_not_found(service):
    with pytest.raises(TaskNotFoundError):
        service.delete_task(999)
