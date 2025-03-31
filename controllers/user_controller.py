from flask import Blueprint, jsonify
from models.user import User

user_bp = Blueprint("user", __name__)

# Beispiel-Daten
users = [
    User(1, "Alice", "alice@example.com"),
    User(2, "Bob", "bob@example.com"),
]

@user_bp.route("/")
def get_users():
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])
