import cv2
import numpy as np
import tensorflow as tf
from sklearn.cluster import KMeans
from matplotlib.colors import rgb_to_hsv

# Load the pre-trained model for classification (MobileNetV2)
def load_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    return model

# Preprocess a single image: resize, normalize, and prepare for the model
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (224, 224))  # Resize to model's expected input
    image_normalized = image_resized / 255.0  # Normalize pixel values to [0, 1]
    image_array = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(image_normalized)[np.newaxis, ...])
    return image_array

# Classify the clothing item (e.g., shirt, pants, etc.)
def classify_item(image_path, model):
    image_array = preprocess_image(image_path)
    predictions = model.predict(image_array)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
    
    # Extract the category from predictions
    item_category = decoded_predictions[0][0][1]
    return item_category

# Detect the dominant color using KMeans clustering. 
# Currently, this detects only one dominant color, which may be sufficient for solids.
# Consider extending this algorithm to detect and return multiple colors (e.g., dominant, secondary, minor)
# or a color palette, especially for multi-colored items. 
# This can provide more detailed insights for complex patterns or designs.
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
