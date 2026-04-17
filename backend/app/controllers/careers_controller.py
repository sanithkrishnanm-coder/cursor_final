from bson import ObjectId
from flask import request

from app.models.base_model import get_collection
from app.utils.responses import success_response, error_response


def list_careers():
    page = max(int(request.args.get("page", 1)), 1)
    limit = max(min(int(request.args.get("limit", 10)), 50), 1)
    skip = (page - 1) * limit
    careers_col = get_collection("careers")
    careers = list(careers_col.find({}, {"_id": 1, "career_title": 1, "description": 1}).skip(skip).limit(limit))
    total = careers_col.count_documents({})
    data = [{"id": str(c["_id"]), "career_title": c["career_title"], "description": c.get("description", "")} for c in careers]
    return success_response({"items": data, "page": page, "limit": limit, "total": total})


def get_career_detail(career_id):
    career = get_collection("careers").find_one({"_id": ObjectId(career_id)})
    if not career:
        return error_response("Career not found", 404)
    return success_response(
        {
            "id": str(career["_id"]),
            "career_title": career["career_title"],
            "description": career.get("description", ""),
            "skills": career.get("skills", []),
            "roadmap": career.get("roadmap", []),
        }
    )
