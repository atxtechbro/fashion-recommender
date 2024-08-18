import tensorflow as tf
from logging_config import get_logger

# Initialize logger
logger = get_logger(__name__)

def preprocess_batch(image_batch):
    logger.info("Starting batch preprocessing for images.")
    processed_batch = tf.map_fn(preprocess_image, image_batch, dtype=tf.float32)
    logger.info("Batch preprocessing completed.")
    return processed_batch

def preprocess_image(image):
    if len(image.shape) == 2:
        logger.info("Image is grayscale; adding channel dimension.")
        image = tf.expand_dims(image, axis=-1)
    
    image_resized = tf.image.resize(image, (224, 224))
    logger.info("Image resized to 224x224.")
    
    if image_resized.shape[-1] == 1:
        logger.info("Image has one channel; converting grayscale to RGB.")
        image_resized = tf.image.grayscale_to_rgb(image_resized)
    
    image_normalized = tf.keras.applications.mobilenet_v2.preprocess_input(image_resized)
    logger.info("Image normalized for MobileNetV2.")
    
    return image_normalized
