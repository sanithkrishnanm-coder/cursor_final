from flask import Blueprint

from app.controllers.admin_controller import create_career
from app.middleware.auth_middleware import jwt_required, roles_required

admin_bp = Blueprint("admin", __name__)

admin_bp.post("/careers")(jwt_required(roles_required("admin")(create_career)))
