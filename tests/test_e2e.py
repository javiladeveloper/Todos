import pytest
from fastapi.testclient import TestClient

from app.config import Settings
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def mock_settings(monkeypatch):
    def fake_settings():
        return Settings(
            log_level="INFO",
            enable_graphql=False,
            lang="en",
            api_title="E2E Mock API",
            api_version="2.0.0",
            api_description="Mocked E2E testing",
            api_contact_name="E2E Tester",
            api_contact_url="https://e2e.test",
            api_contact_email="tester@e2e.test",
        )

    monkeypatch.setattr("app.config.get_settings", fake_settings)


def test_create_task():
    response = client.post(
        "/api/v1/tasks/",
        json={
            "title": "Aprender FastAPI",
            "description": "Leer documentación",
            "completed": False,
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Aprender FastAPI"


def test_get_all_tasks():
    response = client.get("/api/v1/tasks/?page=1&page_size=10")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data


def test_get_task_by_id():
    create = client.post(
        "/api/v1/tasks/",
        json={"title": "Test por ID", "description": "detalle", "completed": False},
    )
    task_id = create.json()["id"]
    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_update_task():
    create = client.post(
        "/api/v1/tasks/",
        json={"title": "Tarea a actualizar", "description": "desc", "completed": False},
    )
    task_id = create.json()["id"]

    response = client.put(
        f"/api/v1/tasks/{task_id}",
        json={"title": "Actualizado", "description": "nueva desc", "completed": True},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Actualizado"


def test_delete_task():
    create = client.post(
        "/api/v1/tasks/",
        json={"title": "Eliminar", "description": "desc", "completed": False},
    )
    task_id = create.json()["id"]

    response = client.delete(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 204

    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 404
