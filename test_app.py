import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}

def test_message(client):
    response = client.get('/message')
    assert response.status_code == 200
    assert response.get_json() == {"message": "This is a message!"}

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert response.get_json() == {"message": "This is the about page!"}

def test_not_found(client):
    response = client.get('/not-found')
    assert response.status_code == 404
    assert response.get_json() == None
