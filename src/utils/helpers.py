import logging
import random
import string

# Create a logger
logger = logging.getLogger(__name__)

class HelperFunctions:
    @staticmethod
    def generate_random_string(length=10):
        """Generate a random string of fixed length."""
        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for i in range(length))
        logger.info("Random string generated successfully.")
        return random_string

    @staticmethod
    def format_date(date):
        """Format a date to a standard string format."""
        if date:
            formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
            logger.info("Date formatted successfully.")
            return formatted_date
        logger.warning("No date provided for formatting.")
        return None

    @staticmethod
    def calculate_age(birthdate):
        """Calculate age from birthdate."""
        from datetime import datetime
        if birthdate:
            today = datetime.today()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            logger.info("Age calculated successfully.")
            return age
        logger.warning("No birthdate provided for age calculation.")
        return None
