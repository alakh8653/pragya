from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Online Learning Platform"}


def test_user_flow():
    # create a user
    payload = {"name": "Alice", "email": "alice@example.com"}
    response = client.post('/users/', json=payload)
    assert response.status_code == 201
    created = response.json()
    assert created['name'] == payload['name']

    # login with created user
    login_resp = client.post('/auth/login', json={"email": payload['email'], "password": "pw"})
    assert login_resp.status_code == 200
    assert 'token' in login_resp.json()
