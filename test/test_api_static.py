from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_version_txt():
    response = client.get("/version.txt")
    assert response.status_code == 200
    assert response.headers.get("content-type") == "text/plain; charset=utf-8"
    assert response.text == "# It will be replaced by docker build\n"


def test_get_favicon():
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.headers.get("content-type") in {
        # Mac hosts
        "image/x-icon",
        # Linux hosts
        "image/vnd.microsoft.icon",
    }


def test_get_robots_txt():
    response = client.get("/robots.txt")
    assert response.status_code == 200
    assert response.headers.get("content-type") == "text/plain; charset=utf-8"
