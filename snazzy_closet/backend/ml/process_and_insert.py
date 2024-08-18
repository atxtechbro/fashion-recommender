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

def classify_item(image_path, model):
    image_array = preprocess_image(image_path)
    predictions = model.predict(image_array[np.newaxis, ...])  # Add batch dimension
    
    # Define your custom categories including the new ones
    wardrobe_categories = ['shirt', 'pants', 'hat', 'shoes', 'belt', 'socks']
    
    # Get the index of the highest predicted probability
    predicted_index = np.argmax(predictions, axis=1)[0]
    
    # Map the index to the corresponding category
    if predicted_index < len(wardrobe_categories):
        predicted_category = wardrobe_categories[predicted_index]
    else:
        predicted_category = "unknown"
    
    return predicted_category

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

def convert_rgb_to_color_name(rgb_color):
    hsv_color = rgb_to_hsv(rgb_color / 255.0)
    hue, saturation, value = hsv_color[0] * 360, hsv_color[1], hsv_color[2]

    if value < 0.2:  # Consider very dark colors as black
        return "black"
    elif value > 0.8 and saturation < 0.2:  # Consider very light colors as white
        return "white"
    elif saturation < 0.25:  # Consider low saturation as grayscale (gray)
        if value < 0.5:
            return "dark gray"
        else:
            return "light gray"

    # Red shades
    if (hue >= 0 and hue < 10) or (hue > 350 and hue <= 360):
        return "red"
    elif hue >= 10 and hue < 25:
        return "orange red"
    elif hue >= 25 and hue < 40:
        return "orange"

    # Yellow shades
    elif hue >= 40 and hue < 60:
        return "yellow orange"
    elif hue >= 60 and hue < 75:
        return "yellow"
    elif hue >= 75 and hue < 85:
        return "lime"

    # Green shades
    elif hue >= 85 and hue < 115:
        return "green"
    elif hue >= 115 and hue < 150:
        return "turquoise green"

    # Cyan/Aqua shades
    elif hue >= 150 and hue < 180:
        return "cyan"
    elif hue >= 180 and hue < 210:
        return "aqua"

    # Blue shades
    elif hue >= 210 and hue < 240:
        return "blue"
    elif hue >= 240 and hue < 270:
        return "indigo"

    # Purple shades
    elif hue >= 270 and hue < 290:
        return "violet"
    elif hue >= 290 and hue < 320:
        return "purple"
    elif hue >= 320 and hue < 335:
        return "magenta"
    elif hue >= 335 and hue < 350:
        return "rose"

    # Fallback for any unclassified colors
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
