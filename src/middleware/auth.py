import jwt
import logging
from functools import wraps
from flask import request, jsonify
from database import session
from user import User  # Assuming a User model exists

# Create a logger
logger = logging.getLogger(__name__)

class AuthMiddleware:
    SECRET_KEY = "your_secret_key"  # Replace with your actual secret key

    @staticmethod
    def token_required(f):
        """Decorator to enforce token-based authentication."""
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].split(" ")[1]

            if not token:
                logger.warning("Token is missing.")
                return jsonify({'message': 'Token is missing!'}), 403

            try:
                data = jwt.decode(token, AuthMiddleware.SECRET_KEY, algorithms=["HS256"])
                current_user = session.query(User).filter_by(id=data['id']).first()
            except Exception as e:
                logger.error(f"Token is invalid: {e}")
                return jsonify({'message': 'Token is invalid!'}), 403

            return f(current_user, *args, **kwargs)
        return decorated

    @staticmethod
    def generate_token(user):
        """Generate a JWT token for a user."""
        token = jwt.encode({'id': user.id}, AuthMiddleware.SECRET_KEY, algorithm="HS256")
        logger.info("Token generated successfully.")
        return token
