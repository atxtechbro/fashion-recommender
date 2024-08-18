import os
import argparse

import numpy as np
import tensorflow as tf

from snazzy_closet.backend.ml.preprocess import preprocess_image
from snazzy_closet.backend.ml.model import build_model


def load_and_preprocess_images(image_dir, batch_size=32):
    images = []
    labels = []
    
    # Assuming your directory structure is image_dir/class_name/image.jpg
    class_names = os.listdir(image_dir)
    class_indices = {class_name: i for i, class_name in enumerate(class_names)}
    
    # Iterate over each class directory
    for class_name in class_names:
        class_dir = os.path.join(image_dir, class_name)
        if not os.path.isdir(class_dir):
            continue
        
        # Iterate over each image file in the class directory
        for image_name in os.listdir(class_dir):
            image_path = os.path.join(class_dir, image_name)
            
            # Preprocess the image using your custom function
            image = preprocess_image(image_path)
            images.append(image)
            
            # Add the corresponding label
            labels.append(class_indices[class_name])
    
    # Convert to numpy arrays and one-hot encode the labels
    images = np.array(images)
    labels = tf.keras.utils.to_categorical(labels, num_classes=len(class_names))
    
    return images, labels

def train_model(model, train_dir, val_dir, epochs=10, batch_size=32):
    # Load and preprocess the training and validation data
    x_train, y_train = load_and_preprocess_images(train_dir, batch_size)
    x_val, y_val = load_and_preprocess_images(val_dir, batch_size)
    
    # Compile the model
    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    # Train the model
    history = model.fit(
        x_train, y_train,
        validation_data=(x_val, y_val),
        epochs=epochs,
        batch_size=batch_size
    )

    model.save('final_model.h5')
    
    return history

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train the Snazzy Closet model on a dataset.")
    parser.add_argument("train_dir", type=str, help="Path to the training data directory.")
    parser.add_argument("val_dir", type=str, help="Path to the validation data directory.")
    parser.add_argument("--epochs", type=int, default=10, help="Number of epochs to train for.")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size for training.")
    
    args = parser.parse_args()
    
    model = build_model(num_classes=5)  # Replace with your actual number of classes
    train_model(model, args.train_dir, args.val_dir, epochs=args.epochs, batch_size=args.batch_size)
