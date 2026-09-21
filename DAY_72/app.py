# Day 72 - Sentiment Analysis Flask API

from flask import Flask, request, jsonify
from sentiment_model import predict_sentiment

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Text Sentiment Analyzer API", "status": "running"})

@app.route("/api/sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must contain JSON data"}), 400

    text = data.get("text")
    if not text:
        return jsonify({"error": "Text field is required"}), 400

    sentiment, confidence = predict_sentiment(text)
    return jsonify({"text": text, "sentiment": sentiment, "confidence": round(confidence, 2)})

if __name__ == "__main__":
    app.run(debug=True)
    
# Done