from flask import Blueprint

from app.controllers.users_controller import get_profile, update_profile
from app.middleware.auth_middleware import jwt_required

users_bp = Blueprint("users", __name__)

users_bp.get("/profile")(jwt_required(get_profile))
users_bp.put("/profile")(jwt_required(update_profile))
