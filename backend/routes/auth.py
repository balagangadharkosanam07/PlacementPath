from flask import Blueprint, request, jsonify, g
from services.auth_service import (
    register_user,
    login_user,
    get_all_users,
    admin_login
)
from middleware.auth_middleware import login_required

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json() or {}

    result = register_user(
        data.get("username"),
        data.get("email"),
        data.get("password")
    )

    return jsonify(result), 201


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json() or {}

    result = login_user(
        data.get("username"),
        data.get("password")
    )

    return jsonify(result), 200


@auth_bp.route("/profile", methods=["GET"])
@login_required
def profile():

    return jsonify({
        "success": True,
        "user": g.current_user
    }), 200


@auth_bp.route("/users", methods=["GET"])
@login_required
def users():

    result = get_all_users()

    return jsonify(result), 200


@auth_bp.route("/admin/login", methods=["POST"])
def admin():

    data = request.get_json() or {}

    result = admin_login(
        data.get("username"),
        data.get("password")
    )

    return jsonify(result), 200


@auth_bp.route("/admin/users", methods=["GET"])
@login_required
def admin_users():

    result = get_all_users()

    return jsonify(result), 200