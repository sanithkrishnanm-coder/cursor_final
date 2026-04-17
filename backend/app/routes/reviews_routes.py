from flask import Blueprint

from app.controllers.reviews_controller import add_review, get_mentor_reviews
from app.middleware.auth_middleware import jwt_required

reviews_bp = Blueprint("reviews", __name__)

reviews_bp.post("/")(jwt_required(add_review))
reviews_bp.get("/mentor/<mentor_id>")(get_mentor_reviews)
