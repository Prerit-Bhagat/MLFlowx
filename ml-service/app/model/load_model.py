import pickle
import os

MODEL_PATH = "app/model/model.pkl"

def load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    return None

# Load once at startup
model = load_model()