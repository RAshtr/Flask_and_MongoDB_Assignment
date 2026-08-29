import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_route(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "UP"

def test_api_route(client):
    response = client.get("/api")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0

def test_home_form_render(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"User Submission Form" in response.data

def test_submit_empty_fields_validation(client):
    response = client.post("/submit", data={"name": "", "email": "", "message": ""})
    assert response.status_code == 400
    assert b"All fields are required" in response.data

def test_submit_invalid_email_validation(client):
    response = client.post("/submit", data={"name": "Ravi", "email": "invalidemail", "message": "Test"})
    assert response.status_code == 400
    assert b"Please enter a valid email address" in response.data