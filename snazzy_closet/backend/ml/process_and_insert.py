import os
from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient

from snazzy_closet.backend.ml.preprocess import load_model, classify_item, detect_color

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['fashion_recommender_db']
collection = db['clothing_items']

# Load the classification model
model = load_model()

photos_dir = 'reference_assets/test_images/'

for image_name in os.listdir(photos_dir):
    image_path = os.path.join(photos_dir, image_name)
    
    if not image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        continue
    
    # Classify item
    item_category = classify_item(image_path, model)
    
    # Detect color
    item_color = detect_color(image_path)
    
    # Create JSON object
    item_data = {
        "_id": ObjectId(),
        "item_name": os.path.basename(image_path).split('.')[0],
        "category": item_category,
        "color": item_color,
        "material": "unknown",  # You can add more advanced processing if needed
        "pattern": "unknown",   # Same here
        "brand": "unknown",     # And here
        "size": "unknown",      # And here
        "image_url": image_path,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    
    collection.insert_one(item_data)
    print(f"Processed and inserted: {item_data['item_name']}")

print("All images have been processed and inserted into the database.")
