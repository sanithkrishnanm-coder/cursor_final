from datetime import datetime, timezone
from flask import request, g

from app.models.base_model import get_collection
from app.utils.responses import success_response
from app.utils.validators import require_fields


def create_booking():
    data = request.get_json() or {}
    require_fields(data, ["mentor_id", "scheduled_at"])
    booking = {
        "mentor_id": data["mentor_id"],
        "user_id": str(g.current_user["_id"]),
        "scheduled_at": data["scheduled_at"],
        "status": "pending",
        "notes": data.get("notes", ""),
        "created_at": datetime.now(timezone.utc),
    }
    get_collection("bookings").insert_one(booking)
    return success_response(message="Booking created", status=201)


def get_user_bookings():
    bookings = list(get_collection("bookings").find({"user_id": str(g.current_user["_id"])}))
    payload = [
        {
            "id": str(b["_id"]),
            "mentor_id": b["mentor_id"],
            "scheduled_at": b["scheduled_at"],
            "status": b.get("status", "pending"),
            "notes": b.get("notes", ""),
        }
        for b in bookings
    ]
    return success_response(payload)
