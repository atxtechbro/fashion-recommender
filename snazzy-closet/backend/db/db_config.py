from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fashion_recommender_db"]

def get_db():
    return db
