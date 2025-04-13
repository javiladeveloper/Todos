from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


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
