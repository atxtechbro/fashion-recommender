# MongoDB Configuration
MONGODB_URI = 'mongodb://localhost:27017/'
DATABASE_NAME = 'fashion_recommender_db'
COLLECTION_NAME = 'clothing_items'

# Training Configuration
BATCH_SIZE = 16
LEARNING_RATE = 0.0001
EPOCHS = 10

# Dataset Paths
TRAINING_LOG_DIR = 'snazzy_closet/backend/ml/training_logs'
PHOTOS_DIR = 'reference_assets/test_images/'

# Model Configuration
MODEL_INPUT_SHAPE = (224, 224, 3)
NUM_CLASSES = 10
