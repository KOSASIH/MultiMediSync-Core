import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base  # Assuming Base is your declarative base
from models import User, Patient, Provider  # Import your models here

# Create a logger
logger = logging.getLogger(__name__)

def setup_database(db_url='sqlite:///multimedisync.db'):
    """Set up the database and create tables."""
    try:
        # Create the database engine
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)  # Create all tables
        logger.info("Database setup completed successfully.")
    except Exception as e:
        logger.error(f"Error setting up the database: {e}")

if __name__ == '__main__':
    setup_database()
