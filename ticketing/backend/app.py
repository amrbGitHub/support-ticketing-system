from flask import Flask, request, jsonify
import os 

app = Flask(__name__)
DEV_TOKEN = os.environ.get("DEV_API_TOKEN")

# First, check the authorization header
@app.before_request
def require_bearer():
    auth = request.headers.get("Authorization", "")
    if not (auth.startswith("Bearer ") and auth.split(" ", 1)[1] == DEV_TOKEN): # if the header isn't "Bearer dev-dev-dev, return unauthorized 401"
        return jsonify({"error": "unauthorized"}), 401
