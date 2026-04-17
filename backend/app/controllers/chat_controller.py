from bson import ObjectId
from flask import request

from app.models.base_model import get_collection
from app.utils.responses import success_response, error_response
from app.utils.security import decode_token
from app.services.chat_service import generate_chat_reply, save_chat_message


def _get_optional_user():
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return None
    token = auth_header.split(" ", 1)[1]
    try:
        payload = decode_token(token)
        return get_collection("users").find_one({"_id": ObjectId(payload["user_id"])})
    except Exception:
        return None


def send_chat_message():
    data = request.get_json() or {}
    message = (data.get("message") or "").strip()
    if not message:
        return error_response("Message is required", 400)

    user = _get_optional_user()
    reply = generate_chat_reply(message, user=user)
    save_chat_message(message, reply, user=user)
    return success_response({"reply": reply}, "Reply generated")


def chat_suggestions():
    return success_response(
        [
            "Suggest careers for me",
            "Show available mentors",
            "How do I book a mentor session?",
            "Show my goals",
        ]
    )
