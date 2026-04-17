from app.routes.auth_routes import auth_bp
from app.routes.users_routes import users_bp
from app.routes.careers_routes import careers_bp
from app.routes.mentors_routes import mentors_bp
from app.routes.bookings_routes import bookings_bp
from app.routes.reviews_routes import reviews_bp
from app.routes.admin_routes import admin_bp
from app.routes.chat_routes import chat_bp


def register_blueprints(app):
    prefix = "/api/v1"
    app.register_blueprint(auth_bp, url_prefix=f"{prefix}/auth")
    app.register_blueprint(users_bp, url_prefix=f"{prefix}/users")
    app.register_blueprint(careers_bp, url_prefix=f"{prefix}/careers")
    app.register_blueprint(mentors_bp, url_prefix=f"{prefix}/mentors")
    app.register_blueprint(bookings_bp, url_prefix=f"{prefix}/bookings")
    app.register_blueprint(reviews_bp, url_prefix=f"{prefix}/reviews")
    app.register_blueprint(admin_bp, url_prefix=f"{prefix}/admin")
    app.register_blueprint(chat_bp, url_prefix=f"{prefix}/chat")
