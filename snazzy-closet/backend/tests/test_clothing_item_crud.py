from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)


def test_create_clothing_item(create_clothing_item):
    # The create_clothing_item fixture already creates the clothing item and yields the item ID.
    item_id = create_clothing_item
    
    # Fetch the created clothing item to confirm it exists
    response = client.get(f"/api/v1/clothing-items/{item_id}")
    assert response.status_code == 200
    assert "_id" in response.json()
    assert response.json()["_id"] == item_id

def test_get_clothing_item(create_clothing_item):
    item_id = create_clothing_item
    response = client.get(f"/api/v1/clothing-items/{item_id}")
    assert response.status_code == 200
    assert response.json()["item_name"] == "Blue T-Shirt"

def test_update_clothing_item(create_clothing_item):
    item_id = create_clothing_item
    response = client.get(f"/api/v1/clothing-items/{item_id}")
    assert response.status_code == 200
    assert response.json()["item_name"] == "Blue T-Shirt"
    assert response.json()["color"] == "#0000FF"

    update_response = client.put(f"/api/v1/clothing-items/{item_id}", json={
        "item_name": "Red T-Shirt",
        "color": "#FF0000"
    })
    assert update_response.status_code == 200
    assert update_response.json()["message"] == "Clothing item updated successfully"

    response = client.get(f"/api/v1/clothing-items/{item_id}")
    assert response.status_code == 200
    assert response.json()["item_name"] == "Red T-Shirt"
    assert response.json()["color"] == "#FF0000"

def test_delete_clothing_item(create_clothing_item):
    item_id = create_clothing_item
    delete_response = client.delete(f"/api/v1/clothing-items/{item_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Clothing item deleted successfully"

    response = client.get(f"/api/v1/clothing-items/{item_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Clothing item not found"
