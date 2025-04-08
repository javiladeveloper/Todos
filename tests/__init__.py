from fastapi.testclient import TestClient
from todolist.main import app

client = TestClient(app)
