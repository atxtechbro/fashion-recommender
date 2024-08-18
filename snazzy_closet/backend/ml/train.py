from .model import build_model
from .preprocess import preprocess_data

def train_model(data, labels):
    model = build_model()
    data = preprocess_data(data)
    model.compile(optimizer="adam", loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=["accuracy"])
    model.fit(data, labels, epochs=5)
    return model
