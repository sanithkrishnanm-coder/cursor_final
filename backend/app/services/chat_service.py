from datetime import datetime, timezone
from bson import ObjectId

from app.models.base_model import get_collection


def _list_top_careers(limit=5):
    careers = list(get_collection("careers").find({}, {"career_title": 1, "description": 1}).limit(limit))
    if not careers:
        return "I could not find careers right now."
    lines = [f"- {c.get('career_title', 'Career')}: {c.get('description', '')}" for c in careers]
    return "Top career paths you can explore:\n" + "\n".join(lines)


def _list_top_mentors(limit=5):
    mentors = list(get_collection("mentors").find({}).limit(limit))
    users = get_collection("users")
    if not mentors:
        return "I could not find mentors right now."
    lines = []
    for mentor in mentors:
        user = users.find_one({"_id": ObjectId(mentor["user_id"])}) if mentor.get("user_id") else None
        name = user["name"] if user else "Mentor"
        skills = ", ".join(mentor.get("skills", [])[:3]) or "General guidance"
        lines.append(f"- {name} ({skills})")
    return "Available mentors:\n" + "\n".join(lines)


def _get_user_booking_status(user_id):
    total = get_collection("bookings").count_documents({"user_id": str(user_id)})
    if total == 0:
        return "You do not have any bookings yet. Open Mentors and book your first session."
    return f"You have {total} booking(s). Open Dashboard to view details."


def generate_chat_reply(message, user=None):
    text = (message or "").strip().lower()

    if any(k in text for k in ["hello", "hi", "hey"]):
        return "Hello! I can help you explore careers, find mentors, track goals, and bookings."
    if "career" in text or "job" in text or "path" in text:
        return _list_top_careers()
    if "mentor" in text or "session" in text:
        return _list_top_mentors()
    if "booking" in text or "appointment" in text:
        if user:
            return _get_user_booking_status(user["_id"])
        return "Please log in to check your booking status, or open Mentors to create a new booking."
    if "goal" in text or "plan" in text:
        if user:
            goals = user.get("goals", [])
            if not goals:
                return "You have no goals saved yet. Open Profile and add your goals."
            return "Your current goals:\n" + "\n".join([f"- {g}" for g in goals])
        return "Log in to view your personalized goals from your profile."

    return (
        "I can help with careers, mentors, bookings, and goals. "
        "Try asking: 'suggest careers', 'show mentors', or 'my bookings'."
    )


def save_chat_message(message, reply, user=None):
    get_collection("chats").insert_one(
        {
            "user_id": str(user["_id"]) if user else None,
            "message": message,
            "reply": reply,
            "created_at": datetime.now(timezone.utc),
        }
    )
