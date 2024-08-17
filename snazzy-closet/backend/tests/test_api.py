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
    assert "id"in response.json()

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
    assert response.json()["gender"] == "Male" # Add more tests for update and delete
