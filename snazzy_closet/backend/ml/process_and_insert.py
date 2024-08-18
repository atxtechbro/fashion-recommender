import os
from datetime import datetime

from bson import ObjectId
import numpy as np
from pymongo import MongoClient
from sklearn.cluster import KMeans
import tensorflow as tf
import cv2
from matplotlib.colors import rgb_to_hsv

from model import load_model
from preprocess import preprocess_image, save_preprocessed_image

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['fashion_recommender_db']
collection = db['clothing_items']

# Load the classification model
model = load_model()

# Function to classify an item
def classify_item(image_path, model):
    image_array = preprocess_image(image_path)
    predictions = model.predict(image_array[np.newaxis, ...])  # Add batch dimension
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
    
    # Extract the category from predictions
    item_category = decoded_predictions[0][0][1]
    return item_category

# Function to detect the dominant color using KMeans clustering
def detect_color(image_path):
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (224, 224))
    image_rgb = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
    pixels = np.float32(image_rgb.reshape(-1, 3))
    
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(pixels)
    
    dominant_color = kmeans.cluster_centers_[0]
    color_name = convert_rgb_to_color_name(dominant_color)
    
    return color_name

# Convert RGB to a human-readable color name
def convert_rgb_to_color_name(rgb_color):
    hsv_color = rgb_to_hsv(rgb_color / 255)
    
    if hsv_color[0] < 15 or hsv_color[0] > 345:
        return "red"
    elif hsv_color[0] < 45:
        return "orange"
    elif hsv_color[0] < 75:
        return "yellow"
    elif hsv_color[0] < 165:
        return "green"
    elif hsv_color[0] < 225:
        return "blue"
    elif hsv_color[0] < 345:
        return "purple"
    else:
        return "unknown"

# Process images and insert into the database
def process_and_insert_images(photos_dir, model, collection):
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
        
        # Insert into the database
        collection.insert_one(item_data)
        print(f"Processed and inserted: {item_data['item_name']}")
        
        # Save preprocessed image
        preprocessed_image = preprocess_image(image_path)
        preprocessed_image_path = os.path.join('output', os.path.basename(image_path))
        save_preprocessed_image(preprocessed_image, preprocessed_image_path)

    print("All images have been processed and inserted into the database.")

if __name__ == "__main__":
    photos_dir = 'reference_assets/test_images/'
    
    # Process images and insert them into the database
    process_and_insert_images(photos_dir, model, collection)
