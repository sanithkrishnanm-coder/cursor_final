from flask import Blueprint

from app.controllers.careers_controller import list_careers, get_career_detail

careers_bp = Blueprint("careers", __name__)

careers_bp.get("/")(list_careers)
careers_bp.get("/<career_id>")(get_career_detail)
