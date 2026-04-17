from werkzeug.exceptions import HTTPException
from app.utils.responses import error_response


def register_error_handlers(app):
    @app.errorhandler(ValueError)
    def handle_value_error(error):
        return error_response(str(error), 400)

    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        return error_response(error.description, error.code)

    @app.errorhandler(Exception)
    def handle_exception(error):
        app.logger.exception("Unhandled exception: %s", error)
        return error_response("Internal server error", 500)
