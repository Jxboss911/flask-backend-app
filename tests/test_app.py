import pytest
from webapp.app import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask Backend App!" in response.data

def test_add(client):
    response = client.get('/add?a=2&b=3')
    assert response.status_code == 200
    assert b"2 + 3 = 5" in response.data

def test_subtract(client):
    response = client.get('/subtract?a=10&b=4')
    assert response.status_code == 200
    assert b"10 - 4 = 6" in response.data