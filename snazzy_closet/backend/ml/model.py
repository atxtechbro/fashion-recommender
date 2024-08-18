import tensorflow as tf

# Load and fine-tune the model for specific wardrobe categories
def load_model(num_classes=4):
    base_model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    
    # Add global average pooling and a dense layer for classification
    model = tf.keras.Sequential([
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(num_classes, activation='softmax')  # Output layer for 4 categories
    ])
    
    return model
