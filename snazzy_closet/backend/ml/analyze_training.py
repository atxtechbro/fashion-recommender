import json
import matplotlib.pyplot as plt
import argparse
import os

def plot_training_history(history_path, output_path=None):
    # Load the training history
    with open(history_path, 'r') as f:
        history = json.load(f)
    
    # Plot accuracy
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(history['accuracy'], label='Train Accuracy')
    plt.plot(history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    
    # Plot loss
    plt.subplot(1, 2, 2)
    plt.plot(history['loss'], label='Train Loss')
    plt.plot(history['val_loss'], label='Validation Loss')
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    # Determine the output path
    if not output_path:
        # Use the same directory as the history file and add an analysis-related suffix
        base_dir = os.path.dirname(history_path)
        base_name = os.path.basename(history_path).replace('.json', '_analysis.png')
        output_path = os.path.join(base_dir, base_name)
    
    # Save the plot to the output path
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot training history from a JSON file.")
    parser.add_argument("history_path", type=str, help="Path to the training history JSON file.")
    parser.add_argument("--output", type=str, help="Path to save the output plot image (optional).")
    
    args = parser.parse_args()
    plot_training_history(args.history_path, args.output)
