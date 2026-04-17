from flask import Blueprint

from app.controllers.mentors_controller import list_mentors, get_mentor_detail

mentors_bp = Blueprint("mentors", __name__)

mentors_bp.get("/")(list_mentors)
mentors_bp.get("/<mentor_id>")(get_mentor_detail)
