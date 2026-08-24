import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_api_route(client):
    response = client.get('/api')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_form_validation_empty_fields(client):
    response = client.post('/', data={"name": "", "email": "", "course": ""})
    assert response.status_code == 200
    assert b"All fields are required" in response.data