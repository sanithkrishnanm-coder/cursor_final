from datetime import datetime, timezone
from flask import request

from app.models.base_model import get_collection
from app.utils.responses import success_response, error_response
from app.utils.security import hash_password, verify_password, create_token
from app.utils.validators import validate_email, require_fields


def register():
    data = request.get_json() or {}
    require_fields(data, ["name", "email", "password"])
    if not validate_email(data["email"]):
        return error_response("Invalid email format", 400)
    users = get_collection("users")
    if users.find_one({"email": data["email"].lower().strip()}):
        return error_response("Email already registered", 409)

    role = data.get("role", "student")
    if role not in ["admin", "mentor", "student"]:
        role = "student"
    user = {
        "name": data["name"].strip(),
        "email": data["email"].lower().strip(),
        "password": hash_password(data["password"]),
        "role": role,
        "goals": data.get("goals", []),
        "created_at": datetime.now(timezone.utc),
    }
    result = users.insert_one(user)
    user["_id"] = result.inserted_id
    if role == "mentor":
        get_collection("mentors").insert_one(
            {
                "user_id": str(result.inserted_id),
                "bio": data.get("bio", ""),
                "skills": data.get("skills", []),
                "hourly_rate": data.get("hourly_rate", 0),
            }
        )
    token = create_token(user)
    return success_response(
        {
            "token": token,
            "user": {"id": str(user["_id"]), "name": user["name"], "email": user["email"], "role": user["role"]},
        },
        "Registration successful",
        201,
    )


def login():
    data = request.get_json() or {}
    require_fields(data, ["email", "password"])
    users = get_collection("users")
    user = users.find_one({"email": data["email"].lower().strip()})
    if not user or not verify_password(data["password"], user["password"]):
        return error_response("Invalid email or password", 401)

    token = create_token(user)
    return success_response(
        {
            "token": token,
            "user": {"id": str(user["_id"]), "name": user["name"], "email": user["email"], "role": user["role"]},
        },
        "Login successful",
    )
