import tensorflow as tf

def preprocess_batch(image_batch):
    # Process each image in the batch individually
    return tf.map_fn(preprocess_image, image_batch, dtype=tf.float32)

def preprocess_image(image):
    # Ensure the image has 3 dimensions (height, width, channels)
    if len(image.shape) == 2:
        # If the image is grayscale (2D), add a channels dimension
        image = tf.expand_dims(image, axis=-1)
    
    # Resize the image to the expected input shape
    image_resized = tf.image.resize(image, (224, 224))
    
    # Convert to RGB if it's grayscale
    if image_resized.shape[-1] == 1:
        image_resized = tf.image.grayscale_to_rgb(image_resized)
    
    # Normalize the image
    image_normalized = tf.keras.applications.mobilenet_v2.preprocess_input(image_resized)
    
    return image_normalized

def load_and_preprocess_fashion_mnist():
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

    # Expand the dimensions to include the channel (for grayscale to RGB conversion)
    X_train = tf.expand_dims(X_train, axis=-1)
    X_test = tf.expand_dims(X_test, axis=-1)

    # Apply preprocessing to each batch
    X_train = preprocess_batch(X_train)
    X_test = preprocess_batch(X_test)
    
    return (X_train, y_train), (X_test, y_test)
