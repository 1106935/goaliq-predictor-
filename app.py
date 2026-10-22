import os
import requests
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

API_KEY = os.environ.get("FOOTBALL_DATA_API_KEY", "")

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/api/health")
def health():
    return jsonify({
        "status": "GoalIQ is running",
        "api_key_configured": bool(API_KEY)
    })

@app.route("/api/fixtures")
def fixtures():
    if not API_KEY:
        return jsonify({
            "error": "Football API key is not configured"
        }), 503

    return jsonify({
        "message": "API connection needs provider-specific configuration",
        "configured": True
    }), 501

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
