import pytest
from fastapi.testclient import TestClient

from app.config import Settings
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def mock_settings(monkeypatch):
    def fake_settings():
        return Settings(
            log_level="WARNING",
            enable_graphql=True,
            lang="en",
            api_title="GraphQL Mock API",
            api_version="9.9.9",
            api_description="GraphQL testing",
            api_contact_name="GraphQL Tester",
            api_contact_url="https://graphql.test",
            api_contact_email="graphql@test.io",
        )

    monkeypatch.setattr("app.config.get_settings", fake_settings)


def graphql_query(query: str):
    return client.post("/graphql", json={"query": query})


def test_graphql_list_tasks():
    query = """
    query {
      tasks {
        id
        title
        completed
      }
    }
    """
    response = graphql_query(query)
    assert response.status_code == 200
    assert "data" in response.json()


def test_graphql_create_task():
    mutation = """
    mutation {
      createTask(input: {
        title: "Test GraphQL",
        description: "GraphQL task",
        completed: false
      }) {
        id
        title
        description
        completed
      }
    }
    """
    response = graphql_query(mutation)
    assert response.status_code == 200
    data = response.json()["data"]["createTask"]
    assert data["title"] == "Test GraphQL"
    assert data["completed"] is False


def test_graphql_get_task():
    query = """
    query {
      task(id: 1) {
        id
        title
      }
    }
    """
    response = graphql_query(query)
    assert response.status_code == 200
    assert response.json()["data"]["task"] is not None


def test_graphql_update_task():
    mutation = """
    mutation {
      updateTask(id: 1, input: {
        title: "Updated",
        description: "Updated desc",
        completed: true
      }) {
        id
        title
        completed
      }
    }
    """
    response = graphql_query(mutation)
    assert response.status_code == 200
    data = response.json()["data"]["updateTask"]
    assert data["title"] == "Updated"
    assert data["completed"] is True


def test_graphql_delete_task():
    mutation = """
    mutation {
      deleteTask(id: 1)
    }
    """
    response = graphql_query(mutation)
    assert response.status_code == 200
    assert response.json()["data"]["deleteTask"] is True
