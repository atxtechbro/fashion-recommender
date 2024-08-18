import tensorflow as tf
from logging_config import get_logger

# Initialize logger
logger = get_logger(__name__)

def build_model(input_shape=(224, 224, 3), num_classes=10):
    logger.info(f"Building model with input shape {input_shape} and {num_classes} output classes.")
    
    base_model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=input_shape)
    logger.info("Loaded base model: MobileNetV2 with ImageNet weights, excluding top layers.")
    
    model = tf.keras.Sequential([
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(num_classes, activation='softmax')  # Adjust number of classes as needed
    ])
    
    logger.info("Model built successfully.")
    return model

def load_model(model_path):
    return tf.keras.models.load_model(model_path)
