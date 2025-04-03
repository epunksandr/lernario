from flask import Blueprint, jsonify
from models.user import User

user_bp = Blueprint("user", __name__)

# Beispiel-Daten

@user_bp.route("/")
def get_users():
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])
