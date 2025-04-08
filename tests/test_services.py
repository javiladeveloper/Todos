import pytest
from fastapi import HTTPException

from todolist import services
from todolist.schemas import TaskCreate, TaskUpdate


def test_create_task_unit():
    data = TaskCreate(title="Unit Task", description="Created", completed=False)
    task = services.create_task(data)
    assert task.id is not None
    assert task.title == "Unit Task"
    assert task.completed is False


def test_get_task_unit():
    task = services.create_task(
        TaskCreate(title="Get Me", description="", completed=False)
    )
    result = services.get_task(task.id)
    assert result.id == task.id
    assert result.title == "Get Me"


def test_update_task_unit():
    task = services.create_task(
        TaskCreate(title="Old", description="", completed=False)
    )
    update_data = TaskUpdate(title="New", description="Changed", completed=True)
    updated = services.update_task(task.id, update_data)
    assert updated.title == "New"
    assert updated.completed is True


def test_delete_task_unit():
    task = services.create_task(
        TaskCreate(title="To Delete", description="", completed=False)
    )
    services.delete_task(task.id)
    try:
        services.get_task(task.id)
        assert False
    except Exception as e:
        assert e.status_code == 404
        assert e.detail == "Task not found"


def test_get_task_not_found():
    with pytest.raises(HTTPException) as exc_info:
        services.get_task(999)
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Task not found"


def test_update_task_not_found():
    data = TaskUpdate(title="X", description="Y", completed=False)
    with pytest.raises(HTTPException) as exc_info:
        services.update_task(999, data)
    assert exc_info.value.status_code == 404


def test_delete_task_not_found():
    with pytest.raises(HTTPException) as exc_info:
        services.delete_task(999)
    assert exc_info.value.status_code == 404
