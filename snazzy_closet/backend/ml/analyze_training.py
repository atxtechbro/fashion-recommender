import json
import matplotlib.pyplot as plt
import os
from config import TRAINING_LOG_DIR

def plot_training_history(history_path):
    # Load the training history
    with open(history_path, 'r') as f:
        history = json.load(f)
    
    # Plot accuracy and loss
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(history['accuracy'], label='Train Accuracy')
    plt.plot(history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(history['loss'], label='Train Loss')
    plt.plot(history['val_loss'], label='Validation Loss')
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    # Save the plot to the configured output path
    base_name = os.path.basename(history_path).replace('.json', '_analysis.png')
    output_path = os.path.join(TRAINING_LOG_DIR, base_name)
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    history_path = os.path.join(TRAINING_LOG_DIR, 'training_history.json')
    plot_training_history(history_path)
