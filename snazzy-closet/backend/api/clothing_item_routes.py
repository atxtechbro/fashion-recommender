from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from ..db.db_config import get_db

router = APIRouter()

db = get_db()

@router.post("/clothing-items/")
def create_clothing_item(clothing_item: dict):
    clothing_item["_id"] = ObjectId()
    clothing_item["created_at"] = datetime.now()
    clothing_item["updated_at"] = datetime.now()
    result = db.clothing_items.insert_one(clothing_item)
    if result.inserted_id:
        return {"_id": str(result.inserted_id)}
    raise HTTPException(status_code=500, detail="Clothing item creation failed")

@router.get("/clothing-items/{item_id}")
def get_clothing_item(item_id: str):
    clothing_item = db.clothing_items.find_one({"_id": ObjectId(item_id)})
    if clothing_item:
        clothing_item["_id"] = str(clothing_item["_id"])
        return clothing_item
    raise HTTPException(status_code=404, detail="Clothing item not found")

@router.put("/clothing-items/{item_id}")
def update_clothing_item(item_id: str, updated_item: dict):
    updated_item["updated_at"] = datetime.now()
    result = db.clothing_items.update_one({"_id": ObjectId(item_id)}, {"$set": updated_item})
    if result.modified_count > 0:
        return {"message": "Clothing item updated successfully"}
    raise HTTPException(status_code=404, detail="Clothing item not found")

@router.delete("/clothing-items/{item_id}")
def delete_clothing_item(item_id: str):
    result = db.clothing_items.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count > 0:
        return {"message": "Clothing item deleted successfully"}
    raise HTTPException(status_code=404, detail="Clothing item not found")
