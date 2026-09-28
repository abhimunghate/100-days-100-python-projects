# Day 79 - Language Translator Flask API

from flask import Flask, jsonify, request
from translator import translate_text

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Day 79 Language Translator API",
        "status": "running",
        "endpoint": "/translate",
        "method": "POST"
    })

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "success": False,
            "error": "JSON request body is required."
        }), 400

    text = data.get("text", "").strip()
    target_lang = data.get("target_lang", "").strip()

    if not text:
        return jsonify({
            "success": False,
            "error": "Text is required."
        }), 400

    if not target_lang:
        return jsonify({
            "success": False,
            "error": "Target language is required."
        }), 400

    try:
        result = translate_text(text, target_lang)
        return jsonify({
            "success": True,
            "original_text": text,
            "translated_text": result["translated_text"],
            "source_language": result["source_language"],
            "target_language": result["target_language"]
        })
    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    
# Done