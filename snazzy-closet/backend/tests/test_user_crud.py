from fastapi.testclient import TestClient

from backend.api.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/api/v1/users/", json={
        "gender": "Male",
        "age": 28,
        "location": "New York",
        "skin_color": "#D2B48C",
        "eye_color": "#0000FF",
        "hair_color": "#000000"
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_user():
    response = client.post("/api/v1/users/", json={
        "gender": "Male",
        "age": 28,
        "location": "New York",
        "skin_color": "#D2B48C",
        "eye_color": "#0000FF",
        "hair_color": "#000000"
    })
    user_id = response.json()["id"]
    
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["gender"] == "Male"

def test_update_user():
    response = client.post("/api/v1/users/", json={
        "gender": "Male",
        "age": 28,
        "location": "New York",
        "skin_color": "#D2B48C",
        "eye_color": "#0000FF",
        "hair_color": "#000000"
    })
    user_id = response.json()["id"]
    
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

def test_delete_user():
    response = client.post("/api/v1/users/", json={
        "gender": "Male",
        "age": 28,
        "location": "New York",
        "skin_color": "#D2B48C",
        "eye_color": "#0000FF",
        "hair_color": "#000000"
    })
    user_id = response.json()["id"]
    
    delete_response = client.delete(f"/api/v1/users/{user_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["msg"] == "User deleted successfully"
    
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
