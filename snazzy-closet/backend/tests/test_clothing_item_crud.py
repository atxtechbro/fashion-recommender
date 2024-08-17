from fastapi.testclient import TestClient

from backend.api.main import app

client = TestClient(app)

def test_create_clothing_item():
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
    assert response.status_code == 200
    assert "_id" in response.json()

def test_get_clothing_item():
    # First, create a clothing item to fetch
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
    
    # Fetch the created clothing item
    response = client.get(f"/api/v1/clothing-items/{item_id}")
    assert response.status_code == 200
    assert response.json()["item_name"] == "Blue T-Shirt"

def test_update_clothing_item():
    # First, create a clothing item to update
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
    
    # Update the clothing item
    update_response = client.put(f"/api/v1/clothing-items/{item_id}", json={
        "item_name": "Red T-Shirt",
        "color": "#FF0000"
    })
    assert update_response.status_code == 200
    assert update_response.json()["message"] == "Clothing item updated successfully"
    
    # Fetch the updated clothing item
    response = client.get(f"/api/v1/clothing-items/{item_id}")
    assert response.status_code == 200
    assert response.json()["item_name"] == "Red T-Shirt"
    assert response.json()["color"] == "#FF0000"

def test_delete_clothing_item():
    # First, create a clothing item to delete
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
    
    # Delete the clothing item
    delete_response = client.delete(f"/api/v1/clothing-items/{item_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Clothing item deleted successfully"
    
    # Try to fetch the deleted clothing item
    response = client.get(f"/api/v1/clothing-items/{item_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Clothing item not found"
