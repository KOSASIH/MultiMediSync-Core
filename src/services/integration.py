import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from patient import Patient
from provider import Provider
from record import Record

# Create a logger
logger = logging.getLogger(__name__)

class IntegrationService:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.bind = self.engine
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def integrate_patient_data(self, patient_data):
        """Integrate patient data from external sources."""
        try:
            patient = Patient(**patient_data)
            self.session.add(patient)
            self.session.commit()
            logger.info("Patient data integrated successfully.")
            return patient
        except Exception as e:
            logger.error(f"Error integrating patient data: {e}")
            self.session.rollback()
            return None

    def integrate_provider_data(self, provider_data):
        """Integrate provider data from external sources."""
        try:
            provider = Provider(**provider_data)
            self.session.add(provider)
            self.session.commit()
            logger.info("Provider data integrated successfully.")
            return provider
        except Exception as e:
            logger.error(f"Error integrating provider data: {e}")
            self.session.rollback()
            return None

    def integrate_record_data(self, record_data):
        """Integrate medical record data from external sources."""
        try:
            record = Record(**record_data)
            self.session.add(record)
            self.session.commit()
            logger.info("Medical record data integrated successfully.")
            return record
        except Exception as e:
            logger.error(f"Error integrating medical record data: {e}")
            self.session.rollback()
            return None
