from datetime import datetime, timezone
from flask import request, g

from app.models.base_model import get_collection
from app.utils.responses import success_response
from app.utils.validators import require_fields


def add_review():
    data = request.get_json() or {}
    require_fields(data, ["mentor_id", "rating", "comment"])
    review = {
        "mentor_id": data["mentor_id"],
        "user_id": str(g.current_user["_id"]),
        "rating": int(data["rating"]),
        "comment": data["comment"].strip(),
        "created_at": datetime.now(timezone.utc),
    }
    get_collection("reviews").insert_one(review)
    return success_response(message="Review submitted", status=201)


def get_mentor_reviews(mentor_id):
    reviews = list(get_collection("reviews").find({"mentor_id": mentor_id}))
    data = [
        {
            "id": str(r["_id"]),
            "rating": r.get("rating", 0),
            "comment": r.get("comment", ""),
            "user_id": r.get("user_id"),
        }
        for r in reviews
    ]
    return success_response(data)
