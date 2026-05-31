from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(
    "models",
    "best_model.pkl"
)

saved_data = joblib.load(MODEL_PATH)

model = saved_data["model"]
classes = saved_data["classes"]


@app.route('/health', methods=['GET'])
def health():

    return {
        "status": "Inference Service Running"
    }


@app.route('/predict', methods=['POST'])
def predict():

    try:

        data = request.json

        df = pd.DataFrame([data])

        prediction = model.predict(df)

        return jsonify({
            "prediction": str(prediction[0])
        })

    except Exception as e:

        return jsonify({
            "status": "failed",
            "error": str(e)
        }), 500


if __name__ == '__main__':

    app.run(
        host="0.0.0.0",
        debug=True,
        port=5002
    )