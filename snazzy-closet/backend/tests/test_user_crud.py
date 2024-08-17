from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)


def test_create_user(create_user):
    # The create_user fixture already creates the user and yields the user ID.
    user_id = create_user
    
    # Fetch the created user to confirm it exists
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    assert "_id" in response.json()
    assert response.json()["_id"] == user_id

def test_get_user(create_user):
    user_id = create_user
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["gender"] == "Male"

def test_update_user(create_user):
    user_id = create_user
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["age"] == 28
    assert response.json()["location"] == "New York"

    update_response = client.put(f"/api/v1/users/{user_id}", json={
        "age": 29,
        "location": "Los Angeles"
    })
    assert update_response.status_code == 200
    assert update_response.json()["msg"] == "User updated successfully"

    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["age"] == 29
    assert response.json()["location"] == "Los Angeles"

def test_delete_user(create_user):
    user_id = create_user
    delete_response = client.delete(f"/api/v1/users/{user_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["msg"] == "User deleted successfully"

    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
