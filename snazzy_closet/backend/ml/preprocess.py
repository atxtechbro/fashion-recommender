import tensorflow as tf

def preprocess_batch(image_batch):
    return preprocess_image(image_batch)

def preprocess_image(image):
    # Ensure the image has 3 or 4 dimensions
    if len(image.shape) == 2:
        # If the image is grayscale (2D), add a channels dimension
        image = tf.expand_dims(image, axis=-1)
    
    if len(image.shape) == 3:
        # Add a batch dimension if missing
        image = tf.expand_dims(image, axis=0)
    
    # Resize the image to the expected input shape
    image_resized = tf.image.resize(image, (224, 224))
    
    # Normalize the image
    image_normalized = tf.keras.applications.mobilenet_v2.preprocess_input(image_resized)
    
    return image_normalized

def load_and_preprocess_fashion_mnist():
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    
    train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
    train_dataset = train_dataset.map(lambda x, y: (preprocess_batch(x), y))
    train_dataset = train_dataset.batch(128)  # Define batch size
    
    test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test))
    test_dataset = test_dataset.map(lambda x, y: (preprocess_batch(x), y))
    test_dataset = test_dataset.batch(128)
    
    return train_dataset, test_dataset
