from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from database import session
from marshmallow import Schema, fields, validate

Base = declarative_base()

class Provider(Base):
    __tablename__ = 'providers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    contact_info = Column(String, nullable=True)
    email = Column(String, nullable=True, unique=True)  # Unique email for notifications
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp for record creation
    updated_at = Column(DateTime, onupdate=datetime.utcnow)  # Timestamp for record updates

    def save(self):
        """Save the provider instance to the database."""
        session.add(self)
        session.commit()
        self.send_notification("Provider record created.")

    def update(self, **kwargs):
        """Update provider attributes."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        self.send_notification("Provider record updated.")

    def delete(self):
        """Delete the provider instance from the database."""
        session.delete(self)
        session.commit()
        self.send_notification("Provider record deleted.")

    def send_notification(self, message):
        """Send a notification to the provider (hypothetical implementation)."""
        if self.email:
            # Here you would integrate with an actual notification service
            print(f"Notification sent to {self.email}: {message}")

    @classmethod
    def get_provider_statistics(cls):
        """Retrieve basic statistics about providers."""
        total_providers = session.query(cls).count()
        return {
            "total_providers": total_providers
        }

class ProviderSchema(Schema):
    """Schema for validating provider data."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    specialty = fields.Str(required=True, validate=validate.Length(min=1))
    contact_info = fields.Str(required=False)
    email = fields.Email(required=False)  # Email validation
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        ordered = True  # Maintain the order of fields
