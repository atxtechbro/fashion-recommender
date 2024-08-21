from pymongo import MongoClient
from snazzy_closet.backend.ml.config import (
    MONGODB_URI,
    DATABASE_NAME,
    COLLECTION_NAME,
    BATCH_SIZE,
    LEARNING_RATE,
    EPOCHS,
    MODEL_INPUT_SHAPE,
    NUM_CLASSES
)

def test_mongodb_configuration():
    # Test MongoDB connection
    client = MongoClient(MONGODB_URI)
    assert client is not None, "Failed to connect to MongoDB"

    # Verify database name
    db = client.get_database(DATABASE_NAME)
    assert db.name == DATABASE_NAME, f"Expected database name {DATABASE_NAME}, got {db.name}"

    # Verify collection name
    collection = db.get_collection(COLLECTION_NAME)
    assert collection.name == COLLECTION_NAME, f"Expected collection name {COLLECTION_NAME}, got {collection.name}"

    # Cleanup: Close the connection
    client.close()

def test_training_configuration():
    assert BATCH_SIZE == 16
    assert LEARNING_RATE == 0.0001
    assert EPOCHS == 10

def test_model_configuration():
    assert MODEL_INPUT_SHAPE == (224, 224, 3)
    assert NUM_CLASSES == 10
