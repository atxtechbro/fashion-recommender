import tensorflow as tf

def build_model(input_shape=(224, 224, 3), num_classes=10):
    base_model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=input_shape)
    model = tf.keras.Sequential([
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(num_classes, activation='softmax')  # Adjust number of classes as needed
    ])
    return model

def load_model(model_path):
    return tf.keras.models.load_model(model_path)
