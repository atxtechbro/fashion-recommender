import tensorflow as tf
import numpy as np

def preprocess_data(data):
    # Example preprocessing code
    data = np.array(data)
    data = data / 255.0
    return data
