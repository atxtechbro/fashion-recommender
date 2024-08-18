import datetime
import os
import json
import tensorflow as tf
from data_loading import load_and_preprocess_fashion_mnist
from model import build_model
from config import BATCH_SIZE, LEARNING_RATE, EPOCHS, TRAINING_LOG_DIR, MODEL_INPUT_SHAPE, NUM_CLASSES

# Load and preprocess the Fashion-MNIST data
train_dataset, test_dataset = load_and_preprocess_fashion_mnist()

# Convert to tf.data.Dataset and batch the data
train_dataset = tf.data.Dataset.from_tensor_slices(train_dataset).batch(BATCH_SIZE)
test_dataset = tf.data.Dataset.from_tensor_slices(test_dataset).batch(BATCH_SIZE)

# Build the model
model = build_model(input_shape=MODEL_INPUT_SHAPE, num_classes=NUM_CLASSES)

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(
    train_dataset,
    validation_data=test_dataset,
    epochs=EPOCHS
)

# Save the model and training history
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
os.makedirs(TRAINING_LOG_DIR, exist_ok=True)

model.save(os.path.join(TRAINING_LOG_DIR, f'fine_tuned_wardrobe_model_{timestamp}.h5'))

history_path = os.path.join(TRAINING_LOG_DIR, f'training_history_{timestamp}.json')
with open(history_path, 'w') as f:
    json.dump(history.history, f)

print(f"Model saved as fine_tuned_wardrobe_model_{timestamp}.h5 in {TRAINING_LOG_DIR}")
print(f"Training history saved as {history_path}")
