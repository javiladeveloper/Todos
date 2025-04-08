from fastapi.testclient import TestClient

from todolist.main import app

client = TestClient(app)


def test_create_task_e2e():
    response = client.post(
        "/tasks/",
        json={"title": "E2E Task", "description": "Via POST", "completed": False},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "E2E Task"


def test_get_all_tasks_e2e():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task_by_id_e2e():
    post = client.post(
        "/tasks/",
        json={"title": "Lookup", "description": "Testing", "completed": False},
    )
    task_id = post.json()["id"]
    response = client.get(f"/tasks/{task_id}/")
    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_update_task_e2e():
    post = client.post(
        "/tasks/", json={"title": "Before", "description": "", "completed": False}
    )
    task_id = post.json()["id"]
    response = client.put(
        f"/tasks/{task_id}/",
        json={"title": "After", "description": "Updated", "completed": True},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "After"
    assert data["completed"] is True


def test_delete_task_e2e():
    post = client.post(
        "/tasks/", json={"title": "Delete Me", "description": "", "completed": False}
    )
    task_id = post.json()["id"]

    del_res = client.delete(f"/tasks/{task_id}/")
    assert del_res.status_code == 204

    get_res = client.get(f"/tasks/{task_id}/")
    assert get_res.status_code == 404
