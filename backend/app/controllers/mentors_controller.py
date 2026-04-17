from bson import ObjectId

from app.models.base_model import get_collection
from app.utils.responses import success_response, error_response


def list_mentors():
    users = get_collection("users")
    mentors_col = get_collection("mentors")
    mentor_docs = list(mentors_col.find({}))
    result = []
    for mentor in mentor_docs:
        user = users.find_one({"_id": ObjectId(mentor["user_id"])})
        if user:
            result.append(
                {
                    "id": str(mentor["_id"]),
                    "user_id": str(user["_id"]),
                    "name": user["name"],
                    "email": user["email"],
                    "bio": mentor.get("bio", ""),
                    "skills": mentor.get("skills", []),
                    "hourly_rate": mentor.get("hourly_rate", 0),
                }
            )
    return success_response(result)


def get_mentor_detail(mentor_id):
    mentor = get_collection("mentors").find_one({"_id": ObjectId(mentor_id)})
    if not mentor:
        return error_response("Mentor not found", 404)
    user = get_collection("users").find_one({"_id": ObjectId(mentor["user_id"])})
    reviews = list(get_collection("reviews").find({"mentor_id": mentor_id}))
    return success_response(
        {
            "id": str(mentor["_id"]),
            "name": user["name"] if user else "Unknown",
            "bio": mentor.get("bio", ""),
            "skills": mentor.get("skills", []),
            "hourly_rate": mentor.get("hourly_rate", 0),
            "reviews_count": len(reviews),
        }
    )
