from fastapi.testclient import TestClient
from backend.main import create_app

app = create_app()

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

    # update user
    update_payload = {"name": "Alice Smith", "email": "alice@example.com"}
    up_resp = client.put(f"/users/{created['id']}", json=update_payload)
    assert up_resp.status_code == 200
    assert up_resp.json()['name'] == 'Alice Smith'

    # delete user
    del_resp = client.delete(f"/users/{created['id']}")
    assert del_resp.status_code == 204


def test_course_and_assignment_flow():
    course_payload = {"title": "Math 101", "description": "Intro"}
    c_resp = client.post('/courses/', json=course_payload)
    assert c_resp.status_code == 201
    course = c_resp.json()

    update_course_payload = {"title": "Math 101 Advanced", "description": "Intro"}
    up_resp = client.put(f"/courses/{course['id']}", json=update_course_payload)
    assert up_resp.status_code == 200
    assert up_resp.json()['title'] == 'Math 101 Advanced'

    assn_payload = {"course_id": course['id'], "title": "Homework 1"}
    a_resp = client.post('/assignments/', json=assn_payload)
    assert a_resp.status_code == 201
    assignment = a_resp.json()

    assn_update = {"title": "Homework 1 updated"}
    au_resp = client.put(f"/assignments/{assignment['id']}", json=assn_update)
    assert au_resp.status_code == 200
    assert au_resp.json()['title'] == 'Homework 1 updated'
