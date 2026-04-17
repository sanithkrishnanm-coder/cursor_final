from flask import g, request

from app.models.base_model import get_collection
from app.utils.responses import success_response


def get_profile():
    user = g.current_user
    return success_response(
        {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "role": user["role"],
            "goals": user.get("goals", []),
        }
    )


def update_profile():
    data = request.get_json() or {}
    updates = {}
    for field in ["name", "goals"]:
        if field in data:
            updates[field] = data[field]
    get_collection("users").update_one({"_id": g.current_user["_id"]}, {"$set": updates})
    return success_response(message="Profile updated")
