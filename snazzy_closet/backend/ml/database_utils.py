from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME

def get_mongo_client(uri=MONGODB_URI):
    return MongoClient(uri)

def get_collection(client, db_name=DATABASE_NAME, collection_name=COLLECTION_NAME):
    db = client[db_name]
    return db[collection_name]

def insert_item(collection, item_data):
    collection.insert_one(item_data)
    print(f"Processed and inserted: {item_data['item_name']}")
