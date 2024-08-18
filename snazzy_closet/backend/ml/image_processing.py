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