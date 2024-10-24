from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from database import session
from marshmallow import Schema, fields, validate

Base = declarative_base()

class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)  # Use DateTime for better handling
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp for record creation
    updated_at = Column(DateTime, onupdate=datetime.utcnow)  # Timestamp for record updates

    # Relationship with patient
    patient = relationship("Patient", back_populates="records")

    def save(self):
        """Save the record instance to the database."""
        session.add(self)
        session.commit()
        self.send_notification("Medical record created.")

    def update(self, **kwargs):
        """Update record attributes."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        self.send_notification("Medical record updated.")

    def delete(self):
        """Delete the record instance from the database."""
        session.delete(self)
        session.commit()
        self.send_notification("Medical record deleted.")

    def send_notification(self, message):
        """Send a notification related to the record (hypothetical implementation)."""
        patient = session.query(Patient).get(self.patient_id)
        if patient and patient.email:
            # Here you would integrate with an actual notification service
            print(f"Notification sent to {patient.email}: {message}")

    @classmethod
    def get_record_statistics(cls):
        """Retrieve basic statistics about medical records."""
        total_records = session.query(cls).count()
        return {
            "total_records": total_records
        }

class RecordSchema(Schema):
    """Schema for validating record data."""
    id = fields.Int(dump_only=True)
    patient_id = fields.Int(required=True)
    description = fields.Str(required=True, validate=validate.Length(min=1))
    date = fields.DateTime(required=False)  # Date can be optional
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        ordered = True  # Maintain the order of fields
