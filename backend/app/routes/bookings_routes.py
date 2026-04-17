from flask import Blueprint

from app.controllers.bookings_controller import create_booking, get_user_bookings
from app.middleware.auth_middleware import jwt_required

bookings_bp = Blueprint("bookings", __name__)

bookings_bp.post("/")(jwt_required(create_booking))
bookings_bp.get("/me")(jwt_required(get_user_bookings))
