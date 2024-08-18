import tensorflow as tf

# Load the pre-trained model for classification (MobileNetV2)
def load_model():
    base_model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    # Add global average pooling and a dense layer for classification
    model = tf.keras.Sequential([
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(1000, activation='softmax')
    ])
    return model
