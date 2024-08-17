from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from ..db.models import user_schema
from ..db.db_config import get_db

router = APIRouter()
db = get_db()
users_collection = db["users"]

@router.post("/users/")
def create_user(user: dict):
    user["_id"] = ObjectId()
    user["created_at"] = datetime.now()
    user["updated_at"] = datetime.now()
    result = users_collection.insert_one(user)
    return {"id": str(result.inserted_id)}

@router.get("/users/{user_id}")
def get_user(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["_id"] = str(user["_id"])
    return user

@router.put("/users/{user_id}")
def update_user(user_id: str, update_data: dict):
    update_data["updated_at"] = datetime.now()
    result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"msg": "User updated successfully"}

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"msg": "User deleted successfully"}
