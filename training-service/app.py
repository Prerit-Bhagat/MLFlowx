from flask import Flask, request, jsonify
import pandas as pd
import os
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

UPLOAD_FOLDER = "datasets"
MODEL_FOLDER = "models"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MODEL_FOLDER, exist_ok=True)


@app.route('/health', methods=['GET'])
def health():

    return {
        "status": "Training Service Running"
    }


@app.route('/train', methods=['POST'])
def train():

    try:

        file = request.files['file']

        target_column = request.form['target_column']

        dataset_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        file.save(dataset_path)

        df = pd.read_csv(dataset_path)

        df.columns = df.columns.str.strip()

        X = df.drop(columns=[target_column])

        y = df[target_column]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        model = RandomForestClassifier()

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        model_path = os.path.join(
            MODEL_FOLDER,
            "best_model.pkl"
        )

        joblib.dump(
            {
                "model": model,
                "classes": list(model.classes_)
            },
            model_path
        )

        return jsonify({
            "status": "success",
            "accuracy": float(accuracy),
            "model_path": model_path,
            "message": "Model trained successfully"
        })

    except Exception as e:

        return jsonify({
            "status": "failed",
            "error": str(e)
        }), 500


if __name__ == '__main__':

    app.run(
        debug=True,
        port=5001
    )