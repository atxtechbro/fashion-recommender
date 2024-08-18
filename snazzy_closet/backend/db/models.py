from bson.objectid import ObjectId
from datetime import datetime

def user_schema():
    return {
        "_id": ObjectId(),
        "gender": "string",
        "age": 0,
        "location": "string",
        "skin_color": "string",
        "eye_color": "string",
        "hair_color": "string",
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

def clothing_item_schema():
    return {
        "_id": ObjectId(),
        "item_name": "string",
        "category": "string",
        "color": "string",
        "material": "string",
        "pattern": "string",
        "brand": "string",
        "size": "string",
        "image_url": "string",
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
