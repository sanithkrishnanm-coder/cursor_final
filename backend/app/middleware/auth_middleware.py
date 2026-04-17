from functools import wraps
from bson import ObjectId
from flask import request, g
from jwt import ExpiredSignatureError, InvalidTokenError

from app.models.base_model import get_collection
from app.utils.responses import error_response
from app.utils.security import decode_token


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return error_response("Missing or invalid token", 401)
        token = auth_header.split(" ", 1)[1]
        try:
            payload = decode_token(token)
            user = get_collection("users").find_one({"_id": ObjectId(payload["user_id"])})
            if not user:
                return error_response("User not found", 401)
            g.current_user = user
        except ExpiredSignatureError:
            return error_response("Token expired", 401)
        except (InvalidTokenError, Exception):
            return error_response("Invalid token", 401)
        return fn(*args, **kwargs)

    return wrapper


def roles_required(*allowed_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user = getattr(g, "current_user", None)
            if not user or user.get("role") not in allowed_roles:
                return error_response("Access denied", 403)
            return fn(*args, **kwargs)

        return wrapper

    return decorator
