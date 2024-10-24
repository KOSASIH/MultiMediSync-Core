import logging
from patient import Patient
from provider import Provider
from record import Record

# Create a logger
logger = logging.getLogger(__name__)

class NotificationService:
    def __init__(self, db_session):
        self.db_session = db_session

    def send_patient_notification(self, patient_id, message):
        """Send a notification to a patient."""
        try:
            patient = self.db_session.query(Patient).get(patient_id)
            if patient and patient.email:
                # Here you would integrate with an actual notification service
                logger.info(f"Notification sent to {patient.email}: {message}")
                return True
            else:
                logger.error("Patient not found or no email address available.")
                return False
        except Exception as e:
            logger.error(f"Error sending patient notification: {e}")
            return False

    def send_provider_notification(self, provider_id, message):
        """Send a notification to a provider."""
        try:
            provider = self.db_session.query(Provider).get(provider_id)
            if provider and provider.email:
                # Here you would integrate with an actual notification service
                logger.info(f"Notification sent to {provider.email}: {message}")
                return True
            else:
                logger.error("Provider not found or no email address available.")
                return False
        except Exception as e:
            logger.error(f"Error sending provider notification: {e}")
            return False

    def send_record_notification(self, record_id, message):
        """Send a notification related to a medical record."""
        try:
            record = self.db_session.query(Record).get(record_id)
            if record and record.patient.email:
                # Here you would integrate with an actual notification service
                logger.info(f"Notification sent to {record.patient.email}: {message}")
                return True
            else:
                logger.error("Medical record not found or no patient email address available.")
                return False
        except Exception as e:
            logger.error(f"Error sending medical record notification: {e}")
            return False
