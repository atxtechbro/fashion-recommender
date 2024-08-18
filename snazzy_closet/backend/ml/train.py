import datetime
import os
import json
import tensorflow as tf
from data_loading import load_and_preprocess_fashion_mnist
from model import build_model
from config import BATCH_SIZE, LEARNING_RATE, EPOCHS, TRAINING_LOG_DIR, MODEL_INPUT_SHAPE, NUM_CLASSES

logger = get_logger(__name__)

def compile_model(model, learning_rate=LEARNING_RATE):
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    logger.info("Model compiled with Adam optimizer and sparse_categorical_crossentropy loss")
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
        logger.info(f"Checkpointing enabled. Checkpoints will be saved in {checkpoint_dir}")

    history = model.fit(
        train_dataset,
        validation_data=test_dataset,
        epochs=epochs,
        callbacks=callbacks
    )
    logger.info(f"Training completed for {epochs} epochs")
    
    return history

def save_training_artifacts(model, history, log_dir=TRAINING_LOG_DIR):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    os.makedirs(log_dir, exist_ok=True)
    
    model_path = os.path.join(log_dir, f'fine_tuned_wardrobe_model_{timestamp}.h5')
    history_path = os.path.join(log_dir, f'training_history_{timestamp}.json')
    
    model.save(model_path)
    
    with open(history_path, 'w') as f:
        json.dump(history.history, f)
    
    logger.info(f"Model saved as {model_path}")
    logger.info(f"Training history saved as {history_path}")

if __name__ == "__main__":
    train_dataset, test_dataset = load_and_preprocess_fashion_mnist()

    train_dataset = tf.data.Dataset.from_tensor_slices(train_dataset).batch(BATCH_SIZE)
    test_dataset = tf.data.Dataset.from_tensor_slices(test_dataset).batch(BATCH_SIZE)

    model = build_model(input_shape=MODEL_INPUT_SHAPE, num_classes=NUM_CLASSES)
    model = compile_model(model)

    history = train_model(model, train_dataset, test_dataset, checkpoint_dir=os.path.join(TRAINING_LOG_DIR, 'checkpoints'))
    
    save_training_artifacts(model, history)
