from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


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


def test_get_openapi_json():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.headers.get("content-type") == "application/json"


def test_get_docs():
    response = client.get("/docs")
    assert response.status_code == 200
    assert response.headers.get("content-type") == "text/html; charset=utf-8"


def test_get_redoc():
    response = client.get("/redoc")
    assert response.status_code == 200
    assert response.headers.get("content-type") == "text/html; charset=utf-8"


def test_get_notfound():
    response = client.get("/notfound")
    assert response.status_code == 404
    assert response.headers.get("content-type") == "application/json"
    assert response.json() == {"detail": "Not Found"}
