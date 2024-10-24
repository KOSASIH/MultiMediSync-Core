import logging
from flask import jsonify

# Create a logger
logger = logging.getLogger(__name__)

class ErrorHandlingMiddleware:
    @staticmethod
    def handle_error(e):
        """Handle errors and return a structured response."""
        logger.error(f"An error occurred: {str(e)}")
        response = {
            "status": "error",
            "message": str(e)
        }
        return jsonify(response), 500

    @staticmethod
    def register(app):
        """Register error handling middleware with the Flask app."""
        @app.errorhandler(Exception)
        def handle_exception(e):
            return ErrorHandlingMiddleware.handle_error(e)
