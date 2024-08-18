import datetime
import os
import json
import tensorflow as tf
from data_loading import load_and_preprocess_fashion_mnist
from model import build_model
from config import BATCH_SIZE, LEARNING_RATE, EPOCHS, TRAINING_LOG_DIR, MODEL_INPUT_SHAPE, NUM_CLASSES

def compile_model(model, learning_rate=LEARNING_RATE):
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def train_model(model, train_dataset, test_dataset, epochs=EPOCHS, checkpoint_dir=None):
    callbacks = []
    
    if checkpoint_dir:
        os.makedirs(checkpoint_dir, exist_ok=True)
        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=os.path.join(checkpoint_dir, 'checkpoint_{epoch:02d}.h5'),
            save_weights_only=True,
            save_freq='epoch'
        )
        callbacks.append(checkpoint_callback)
    
    history = model.fit(
        train_dataset,
        validation_data=test_dataset,
        epochs=epochs,
        callbacks=callbacks
    )
    
    return history

def save_training_artifacts(model, history, log_dir=TRAINING_LOG_DIR):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    os.makedirs(log_dir, exist_ok=True)
    
    model_path = os.path.join(log_dir, f'fine_tuned_wardrobe_model_{timestamp}.h5')
    history_path = os.path.join(log_dir, f'training_history_{timestamp}.json')
    
    model.save(model_path)
    
    with open(history_path, 'w') as f:
        json.dump(history.history, f)
    
    print(f"Model saved as {model_path}")
    print(f"Training history saved as {history_path}")

if __name__ == "__main__":
    # Load and preprocess the Fashion-MNIST data
    train_dataset, test_dataset = load_and_preprocess_fashion_mnist()

    # Convert to tf.data.Dataset and batch the data
    train_dataset = tf.data.Dataset.from_tensor_slices(train_dataset).batch(BATCH_SIZE)
    test_dataset = tf.data.Dataset.from_tensor_slices(test_dataset).batch(BATCH_SIZE)

    # Build the model
    model = build_model(input_shape=MODEL_INPUT_SHAPE, num_classes=NUM_CLASSES)
    
    # Compile the model
    model = compile_model(model)

    # Train the model with checkpointing
    history = train_model(model, train_dataset, test_dataset, checkpoint_dir=os.path.join(TRAINING_LOG_DIR, 'checkpoints'))
    
    # Save the model and training history
    save_training_artifacts(model, history)
