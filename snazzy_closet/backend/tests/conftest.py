import pytest
from fastapi.testclient import TestClient

from snazzy_closet.backend.api.main import app

client = TestClient(app)

@pytest.fixture
def create_user():
    response = client.post("/api/v1/users/", json={
        "gender": "Male",
        "age": 28,
        "location": "New York",
        "skin_color": "#D2B48C",
        "eye_color": "#0000FF",
        "hair_color": "#000000"
    })
    user_id = response.json()["id"]
    yield user_id
    client.delete(f"/api/v1/users/{user_id}")

@pytest.fixture
def create_clothing_item():
    response = client.post("/api/v1/clothing-items/", json={
        "item_name": "Blue T-Shirt",
        "category": "Shirt",
        "color": "#0000FF",
        "material": "Cotton",
        "pattern": "Solid",
        "brand": "Uniqlo",
        "size": "M",
        "image_url": "http://example.com/image.jpg"
    })
    item_id = response.json()["_id"]
    yield item_id
    client.delete(f"/api/v1/clothing-items/{item_id}")
