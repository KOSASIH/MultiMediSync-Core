import logging
from patient import Patient
from provider import Provider
from record import Record

# Create a logger
logger = logging.getLogger(__name__)

class AnalyticsService:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_patient_statistics(self):
        """Retrieve basic statistics about patients."""
        try:
            total_patients = self.db_session.query(Patient).count()
            average_age = self.db_session.query(Patient.age).avg()
            logger.info("Patient statistics retrieved successfully.")
            return {
                "total_patients": total_patients,
                "average_age": average_age
            }
        except Exception as e:
            logger.error(f"Error retrieving patient statistics: {e}")
            return None

    def get_provider_statistics(self):
        """Retrieve basic statistics about providers."""
        try:
            total_providers = self.db_session.query(Provider).count()
            logger.info("Provider statistics retrieved successfully.")
            return {
                "total_providers": total_providers
            }
        except Exception as e:
            logger.error(f"Error retrieving provider statistics: {e}")
            return None

    def get_record_statistics(self):
        """Retrieve basic statistics about medical records."""
        try:
            total_records = self.db_session.query(Record).count()
            logger.info("Medical record statistics retrieved successfully.")
            return {
                "total_records": total_records
            }
        except Exception as e:
            logger.error(f"Error retrieving medical record statistics: {e}")
            return None
