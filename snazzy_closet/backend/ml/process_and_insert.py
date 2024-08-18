import os
from datetime import datetime

from bson import ObjectId
import numpy as np
from sklearn.cluster import KMeans
import cv2
from matplotlib.colors import rgb_to_hsv

from model import load_model
from image_processing import preprocess_image
from config import PHOTOS_DIR
from database_utils import get_mongo_client, get_collection, insert_item

# Load the classification model
model = load_model()

def classify_item(image_path, model):
    image_array = preprocess_image(image_path)
    predictions = model.predict(image_array[np.newaxis, ...])  # Add batch dimension
    
    wardrobe_categories = ['shirt', 'pants', 'hat', 'shoes', 'belt', 'socks']
    predicted_index = np.argmax(predictions, axis=1)[0]
    return wardrobe_categories[predicted_index] if predicted_index < len(wardrobe_categories) else "unknown"

def detect_color(image_path):
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (224, 224))
    image_rgb = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
    pixels = np.float32(image_rgb.reshape(-1, 3))
    
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(pixels)
    
    return convert_rgb_to_color_name(kmeans.cluster_centers_[0])

def convert_rgb_to_color_name(rgb_color):
    hsv_color = rgb_to_hsv(rgb_color / 255.0)
    hue, saturation, value = hsv_color[0] * 360, hsv_color[1], hsv_color[2]

    if value < 0.2:
        return "black"
    elif value > 0.8 and saturation < 0.2:
        return "white"
    elif saturation < 0.25:
        return "dark gray" if value < 0.5 else "light gray"

    if (hue >= 0 and hue < 10) or (hue > 350 and hue <= 360):
        return "red"
    elif hue >= 10 and hue < 25:
        return "orange red"
    elif hue >= 25 and hue < 40:
        return "orange"
    elif hue >= 40 and hue < 60:
        return "yellow orange"
    elif hue >= 60 and hue < 75:
        return "yellow"
    elif hue >= 75 and hue < 85:
        return "lime"
    elif hue >= 85 and hue < 115:
        return "green"
    elif hue >= 115 and hue < 150:
        return "turquoise green"
    elif hue >= 150 and hue < 180:
        return "cyan"
    elif hue >= 180 and hue < 210:
        return "aqua"
    elif hue >= 210 and hue < 240:
        return "blue"
    elif hue >= 240 and hue < 270:
        return "indigo"
    elif hue >= 270 and hue < 290:
        return "violet"
    elif hue >= 290 and hue < 320:
        return "purple"
    elif hue >= 320 and hue < 335:
        return "magenta"
    elif hue >= 335 and hue < 350:
        return "rose"

    return "unknown"

def process_and_insert_images(photos_dir, model, collection):
    for image_name in os.listdir(photos_dir):
        image_path = os.path.join(photos_dir, image_name)
        
        if not image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            continue
        
        item_category = classify_item(image_path, model)
        item_color = detect_color(image_path)
        
        item_data = {
            "_id": ObjectId(),
            "item_name": os.path.basename(image_path).split('.')[0],
            "category": item_category,
            "color": item_color,
            "material": "unknown",
            "pattern": "unknown",
            "brand": "unknown",
            "size": "unknown",
            "image_url": image_path,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        insert_item(collection, item_data)

    print("All images have been processed and inserted into the database.")

if __name__ == "__main__":
    client = get_mongo_client()
    collection = get_collection(client)
    process_and_insert_images(PHOTOS_DIR, model, collection)
