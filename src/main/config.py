import os

class Config:
    """Configuration class for the application."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1']
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///app.db'
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

    @staticmethod
    def init_app(app):
        """Initialize the app with the configuration."""
        pass
