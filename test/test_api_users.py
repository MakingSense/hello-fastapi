from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_users():
    response = client.get("/users/", headers={"X-TOKEN": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.headers.get("content-type") == "application/json"


def test_get_user():
    response = client.get("/users/aaa", headers={"X-TOKEN": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.headers.get("content-type") == "application/json"
    assert response.json() == {"username": "aaa"}


def test_get_me_user():
    response = client.get("/users/me", headers={"X-TOKEN": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.headers.get("content-type") == "application/json"
    assert response.json() == {"username": "fake_current_user"}
