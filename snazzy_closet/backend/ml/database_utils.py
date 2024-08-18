from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME
from logging_config import get_logger

# Initialize logger
logger = get_logger(__name__)

def get_mongo_client(uri=MONGODB_URI):
    logger.info(f"Connecting to MongoDB at {uri}.")
    client = MongoClient(uri)
    logger.info("MongoDB connection established.")
    return client

def get_collection(client, db_name=DATABASE_NAME, collection_name=COLLECTION_NAME):
    logger.info(f"Accessing collection '{collection_name}' in database '{db_name}'.")
    db = client[db_name]
    collection = db[collection_name]
    logger.info(f"Collection '{collection_name}' accessed successfully.")
    return collection

def insert_item(collection, item_data):
    logger.info(f"Inserting item: {item_data['item_name']} into collection.")
    collection.insert_one(item_data)
    logger.info(f"Item '{item_data['item_name']}' successfully inserted.")
