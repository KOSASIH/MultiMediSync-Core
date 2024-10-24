import os
import logging
from alembic import command
from alembic.config import Config

# Create a logger
logger = logging.getLogger(__name__)

def run_migrations():
    """Run database migrations using Alembic."""
    try:
        alembic_cfg = Config("alembic.ini")  # Path to your Alembic config file
        command.upgrade(alembic_cfg, "head")  # Upgrade to the latest version
        logger.info("Database migrations completed successfully.")
    except Exception as e:
        logger.error(f"Error running migrations: {e}")

if __name__ == '__main__':
    run_migrations()
