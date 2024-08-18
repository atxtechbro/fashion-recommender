import datetime
import os
import json
import tensorflow as tf
from preprocess import load_and_preprocess_fashion_mnist
from model import build_model

# Load and preprocess the Fashion-MNIST data
train_dataset, test_dataset = load_and_preprocess_fashion_mnist()

# Build the model
model = build_model(input_shape=(224, 224, 3), num_classes=10)

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(
    train_dataset,
    validation_data=test_dataset,
    epochs=10
)

# Save the model and training history
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
log_dir = 'snazzy_closet/backend/ml/training_logs'
os.makedirs(log_dir, exist_ok=True)

model.save(os.path.join(log_dir, f'fine_tuned_wardrobe_model_{timestamp}.h5'))

history_path = os.path.join(log_dir, f'training_history_{timestamp}.json')
with open(history_path, 'w') as f:
    json.dump(history.history, f)

print(f"Model saved as fine_tuned_wardrobe_model_{timestamp}.h5 in {log_dir}")
print(f"Training history saved as {history_path}")
