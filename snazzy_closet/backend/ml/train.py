import datetime
import json
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Step 1: Prepare the Dataset
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'dataset/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='sparse'
)

validation_generator = validation_datagen.flow_from_directory(
    'dataset/validation',
    target_size=(224, 224),
    batch_size=32,
    class_mode='sparse'
)

# Step 2: Load the Pre-Trained Model
base_model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Step 3: Replace the Top Layer with a New Classifier for 6 Categories
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(6, activation='softmax')  # 6 categories: shirt, pants, hat, shoes, belt, socks
])

# Step 4: Compile the Model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Step 5: Fine-Tune the Model
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=10
)

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# Save the model with the timestamp in the filename
model.save(f'fine_tuned_wardrobe_model_{timestamp}.h5')

# Save the training history
history_path = f'training_history_{timestamp}.json'
with open(history_path, 'w') as f:
    json.dump(history.history, f)

print(f"Model saved as fine_tuned_wardrobe_model_{timestamp}.h5")
print(f"Training history saved as {history_path}")
