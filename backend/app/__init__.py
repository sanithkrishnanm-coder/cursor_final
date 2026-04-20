from flask import Flask
from flask_cors import CORS

from config import Config
from app.models.base_model import init_db
from app.middleware.error_handler import register_error_handlers
from app.routes import register_blueprints
from app.services.seed_service import seed_default_careers
from app.utils.logger import setup_logging


def create_app():
    app = Flask(__name__)
    # Avoid 308 redirects caused by trailing slash mismatches in API routes.
    app.url_map.strict_slashes = False
    app.config.from_object(Config)

    setup_logging(app)
    init_db(app)
    seed_default_careers()

    CORS(
    app,
    resources={r"/*": {"origins": "https://career-guidance-frontend-tau.vercel.app"}},
    supports_credentials=True,
)

    register_error_handlers(app)
    register_blueprints(app)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app
app = create_app()
