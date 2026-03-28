from flask import Blueprint, request, jsonify
from app.services.prediction_service import predict

main = Blueprint("main", __name__)

@main.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ML service running"}), 200


@main.route("/predict", methods=["POST"])
def predict_route():
    try:
        data = request.get_json()

        result = predict(data)

        return jsonify({
            "prediction": result
        }), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500