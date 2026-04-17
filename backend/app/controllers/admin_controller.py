from flask import request

from app.models.base_model import get_collection
from app.utils.responses import success_response
from app.utils.validators import require_fields


def create_career():
    data = request.get_json() or {}
    require_fields(data, ["career_title", "description"])
    career = {
        "career_title": data["career_title"].strip(),
        "description": data["description"].strip(),
        "skills": data.get("skills", []),
        "roadmap": data.get("roadmap", []),
    }
    get_collection("careers").insert_one(career)
    return success_response(message="Career added", status=201)
