#!/usr/bin/env python3
"""
task_04_flask.py

Simple Flask API for the learning project.

Endpoints:
  GET  /               -> "Welcome to the Flask API!"
  GET  /status         -> "OK"
  GET  /data           -> JSON list of usernames (e.g. ["jane","john"])
  GET  /users/<u>      -> JSON user object or 404 {"error":"User not found"}
  POST /add_user       -> Add a user (expects JSON). Responses:
                           201 {"message":"User added","user":{...}}
                           400 {"error":"Invalid JSON"} (bad body)
                           400 {"error":"Username is required"} (missing username)
                           409 {"error":"Username already exists"} (duplicate)
"""

from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Start with an empty user store to avoid test pollution.
# users: dict mapping username -> user dict (which includes 'username' key)
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def list_usernames():
    # Return a JSON list of usernames
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    # Parse JSON safely, return 400 for invalid JSON
    try:
        data = request.get_json(force=False)
    except BadRequest:
        return jsonify({"error": "Invalid JSON"}), 400

    # get_json returns None if no JSON body or invalid JSON
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Must be a mapping/dict
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check duplicate
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Build user object including username
    user_obj = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201


# Allow running directly with `python3 task_04_flask.py`
if __name__ == "__main__":
    # Note: in testing environment they commonly run `flask --app task_04_flask.py run`
    # but we also allow running directly for convenience.
    app.run(host="127.0.0.1", port=5000)