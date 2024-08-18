import cv2
import numpy as np
import tensorflow as tf

# Preprocess a single image: resize, normalize, and prepare for the model
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Error loading image at {image_path}")
    
    image_resized = cv2.resize(image, (224, 224))  # Resize to model's expected input
    image_normalized = tf.keras.applications.mobilenet_v2.preprocess_input(image_resized)
    return image_normalized

# Save the preprocessed image to a file
def save_preprocessed_image(preprocessed_image, output_path):
    # Convert back to [0, 255] range from [-1, 1]
    image_display = (preprocessed_image + 1.0) * 127.5
    image_display = np.clip(image_display, 0, 255).astype(np.uint8)
    
    # Save the image to a file using OpenCV
    cv2.imwrite(output_path, image_display)
