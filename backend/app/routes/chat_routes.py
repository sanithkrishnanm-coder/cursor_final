from flask import Blueprint

from app.controllers.chat_controller import send_chat_message, chat_suggestions

chat_bp = Blueprint("chat", __name__)

chat_bp.post("/message")(send_chat_message)
chat_bp.get("/suggestions")(chat_suggestions)
