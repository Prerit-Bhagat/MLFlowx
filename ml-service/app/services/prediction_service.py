from app.model.load_model import model
import numpy as np

def validate_input(data):
    if not data:
        raise ValueError("No input data provided")

    if "year" not in data or "kmDriven" not in data:
        raise ValueError("Missing fields: year, kmDriven")

    try:
        year = int(data["year"])
        km = int(data["kmDriven"])
    except:
        raise ValueError("Invalid input types")

    return year, km


def predict(data):
    year, km = validate_input(data)

    # 🔥 If model exists → use it
    if model:
        prediction = model.predict(np.array([[year, km]]))[0]
    else:
        # fallback dummy logic
        prediction = year * 10 - km // 100

    return int(prediction)