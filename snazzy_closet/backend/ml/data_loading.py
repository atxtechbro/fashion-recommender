from tensorflow import tf

from image_processing import preprocess_batch


def load_and_preprocess_fashion_mnist():
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

    # Expand the dimensions to include the channel (for grayscale to RGB conversion)
    X_train = tf.expand_dims(X_train, axis=-1)
    X_test = tf.expand_dims(X_test, axis=-1)

    # Apply preprocessing to each batch
    X_train = preprocess_batch(X_train)
    X_test = preprocess_batch(X_test)

    return (X_train, y_train), (X_test, y_test)
