from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_post_admin_with_token():
    response = client.post("/admin/?token=jessica")
    assert response.status_code == 200
    assert response.json() == {"message": "Admin getting schwifty"}


def test_post_admin_without_token():
    response = client.post("/admin/")
    assert response.status_code == 400
    assert response.json() == {"detail": "No Jessica token provided"}


def test_get_admin_without_token():
    response = client.get("/admin/")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}
