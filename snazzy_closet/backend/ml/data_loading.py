import tensorflow as tf
from image_processing import preprocess_batch
from logging_config import get_logger

# Initialize logger
logger = get_logger(__name__)

def load_and_preprocess_fashion_mnist():
    logger.info("Loading the Fashion-MNIST dataset.")
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    logger.info(f"Dataset loaded successfully with {X_train.shape[0]} training samples and {X_test.shape[0]} test samples.")

    logger.info("Expanding dimensions to include the channel for grayscale to RGB conversion.")
    X_train = tf.expand_dims(X_train, axis=-1)
    X_test = tf.expand_dims(X_test, axis=-1)
    logger.info("Dimension expansion completed.")

    logger.info("Applying preprocessing to each batch.")
    X_train = preprocess_batch(X_train)
    X_test = preprocess_batch(X_test)
    logger.info("Preprocessing completed.")

    return (X_train, y_train), (X_test, y_test)
