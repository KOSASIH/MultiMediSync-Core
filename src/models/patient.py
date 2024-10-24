from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from database import session
from marshmallow import Schema, fields, validate

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    medical_history = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp for record creation
    updated_at = Column(DateTime, onupdate=datetime.utcnow)  # Timestamp for record updates
    email = Column(String, nullable=True, unique=True)  # Unique email for notifications

    # Relationship with medical records
    records = relationship("Record", back_populates="patient")

    def save(self):
        """Save the patient instance to the database."""
        session.add(self)
        session.commit()
        self.send_notification("Patient record created.")

    def update(self, **kwargs):
        """Update patient attributes."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        self.send_notification("Patient record updated.")

    def delete(self):
        """Delete the patient instance from the database."""
        session.delete(self)
        session.commit()
        self.send_notification("Patient record deleted.")

    def send_notification(self, message):
        """Send a notification to the patient (hypothetical implementation)."""
        if self.email:
            # Here you would integrate with an actual notification service
            print(f"Notification sent to {self.email}: {message}")

    @classmethod
    def get_patient_statistics(cls):
        """Retrieve basic statistics about patients."""
        total_patients = session.query(cls).count()
        average_age = session.query(func.avg(cls.age)).scalar()
        return {
            "total_patients": total_patients,
            "average_age": average_age
        }

class PatientSchema(Schema):
    """Schema for validating patient data."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    age = fields.Int(required=True, validate=validate.Range(min=0))
    gender = fields.Str(required=True, validate=validate.OneOf(["male", "female", "other"]))
    medical_history = fields.List(fields.Str(), required=False)
    email = fields.Email(required=False)  # Email validation
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        ordered = True  # Maintain the order of fields
