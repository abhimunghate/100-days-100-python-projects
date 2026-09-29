# This is Day 80 project : Fake News Detector
# Flask REST API

import os
import re
import joblib
import nltk
from flask import Flask, jsonify, request
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

MODEL_PATH = "models/fake_news_model.pkl"
VECTORIZER_PATH = ("models/tfidf_vectorizer.pkl")

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

try:
    nltk.download("punkt_tab", quiet=True)
except Exception:
    pass

stop_words = set(stopwords.words("english"))

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model not found. Run train_model.py first.")

if not os.path.exists(VECTORIZER_PATH):
    raise FileNotFoundError("TF-IDF vectorizer not found. Run train_model.py first.")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

app = Flask(__name__)

def clean_text(text):
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words and len(word) > 2]
    return " ".join(tokens)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "Day 80 - Fake News Detector",
        "status": "running",
        "model": "TF-IDF + Random Forest",
        "endpoint": "/predict",
        "method": "POST"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "success": False,
            "error": ("JSON request body is required.")
        }), 400

    title = data.get("title", "").strip()
    text = data.get("text", "").strip()
    if not title and not text:
        return jsonify({
            "success": False,
            "error": ("Please provide title or text.")
        }), 400

    combined_text = (title + " " + text)
    cleaned_text = clean_text(combined_text)
    if not cleaned_text:
        return jsonify({
            "success": False,
            "error": ("The supplied text could not be processed.")
        }), 400

    try:
        features = vectorizer.transform([cleaned_text])
        prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]
        confidence = float(max(probabilities) * 100)

        if prediction == 1:
            label = "REAL NEWS"
        else:
            label = "FAKE NEWS"

        return jsonify({
            "success": True,
            "prediction": label,
            "confidence": round(confidence, 2),
            "model": ("TF-IDF + Random Forest"),
            "note": ("This is a machine-learning classification result, not independent fact verification.")
        })
    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    
# Done