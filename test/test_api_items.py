from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_items():
    response = client.get("/items/", headers={"X-TOKEN": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.headers.get("content-type") == "application/json"


def test_get_item():
    response = client.get(
        "/items/plumbus", headers={"X-TOKEN": "fake-super-secret-token"}
    )
    assert response.status_code == 200
    assert response.headers.get("content-type") == "application/json"


def test_get_items_without_token():
    response = client.get("/items/")
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Token header invalid"}
