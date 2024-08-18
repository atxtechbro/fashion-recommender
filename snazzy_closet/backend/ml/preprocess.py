import tensorflow as tf

def preprocess_image(image):
    image = tf.image.resize(image, (224, 224))
    image = tf.image.grayscale_to_rgb(image)  # Convert to RGB
    image = image / 255.0  # Normalize to [0, 1]
    return image

def preprocess_batch(batch):
    return preprocess_image(batch)

def load_and_preprocess_fashion_mnist():
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    
    train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
    train_dataset = train_dataset.map(lambda x, y: (preprocess_batch(x), y))
    train_dataset = train_dataset.batch(128)  # Define batch size
    
    test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test))
    test_dataset = test_dataset.map(lambda x, y: (preprocess_batch(x), y))
    test_dataset = test_dataset.batch(128)
    
    return train_dataset, test_dataset
