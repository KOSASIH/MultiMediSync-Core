import logging
import sys

def setup_logging():
    """Setup logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),  # Log to standard output
            logging.FileHandler('app.log')      # Log to a file
        ]
    )
    logging.info("Logging is set up.")
