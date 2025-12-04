#!/usr/bin/env python3
"""
task_05_security.py

Flask app demonstrating:
 - Basic HTTP Authentication (Flask-HTTPAuth)
 - JWT token issuance and protection (Flask-JWT-Extended)
 - Role-based access control for an admin-only endpoint

Endpoints:
 - GET  /basic-protected   -> Basic Auth protected (returns "Basic Auth: Access Granted")
 - POST /login             -> JSON {username, password} -> returns {access_token: "..."}
 - GET  /jwt-protected     -> JWT protected (returns "JWT Auth: Access Granted")
 - GET  /admin-only        -> JWT protected + role check (returns "Admin Access: Granted" or 403)
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Use a deterministic secret for the learning environment/tests.
# In production use a secure random secret and load from environment.
app.config["JWT_SECRET_KEY"] = "super-secret-key-for-testing-only"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users dict for demo/testing:
# Passwords are hashed.
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}

# -----------------------
# Basic HTTP Auth handlers
# -----------------------
@auth.verify_password
def verify_password(username, password):
    if not username or not password:
        return False
    u = users.get(username)
    if not u:
        return False
    return check_password_hash(u["password"], password)


@auth.error_handler
def basic_auth_error():
    # Return 401 with WWW-Authenticate header (Flask-HTTPAuth sets it automatically),
    # and JSON body for automated checks.
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -----------------------
# JWT Authentication
# -----------------------
@app.route("/login", methods=["POST"])
def login():
    # parse JSON safely
    try:
        data = request.get_json(force=False)
    except BadRequest:
        return jsonify({"error": "Invalid JSON"}), 400

    if data is None or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        # For missing creds, return 401
        return jsonify({"error": "Bad credentials"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad credentials"}), 401

    # Include role in identity so we can check it later
    additional_claims = {"role": user.get("role", "user")}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)

    return jsonify({"access_token": access_token})


# JWT error handlers - return 401 for all auth-related JWT errors (per instructions)
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    # Missing Authorization header or no token present
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    # Token couldn't be parsed or is otherwise invalid
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    # Token has expired
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    # Token revoked (if using token revocation list)
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# A generic protected endpoint
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    # If we reached here, token is valid
    return "JWT Auth: Access Granted"


# Admin-only endpoint with role check
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    # get_jwt_identity() returns the identity (username)
    identity = get_jwt_identity()
    # We stored role in additional claims; fetch role from request context via get_jwt_identity? Not available.
    # Flask-JWT-Extended v4 allows reading claims with get_jwt(). But to avoid version-specific calls that tests
    # may not expect, we'll decode the claims via request context if available.
    # Safer approach: use flask_jwt_extended.get_jwt() to access claims.
    try:
        from flask_jwt_extended import get_jwt
        claims = get_jwt()
        role = claims.get("role", "user")
    except Exception:
        # Fallback if get_jwt not available
        role = "user"

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# Allow running directly
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)