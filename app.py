from flask import Flask, request, jsonify
import joblib

# Load model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h2>📧 Phishing Mail Detection API</h2><p>Use /predict (POST) with JSON {'text': 'your email here'} to classify.</p>"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    email_text = data.get("text", "")

    if not email_text:
        return jsonify({"error": "No text provided"}), 400

    # Transform text and predict
    X = vectorizer.transform([email_text])
    prediction = model.predict(X)[0]

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
