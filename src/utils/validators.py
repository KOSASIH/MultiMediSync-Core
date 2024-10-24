import re
from marshmallow import ValidationError

class InputValidators:
    @staticmethod
    def validate_email(email):
        """Validate email format."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValidationError("Invalid email format.")

    @staticmethod
    def validate_phone(phone):
        """Validate phone number format."""
        phone_regex = r'^\+?[1-9]\d{1,14}$'  # E.164 format
        if not re.match(phone_regex, phone):
            raise ValidationError("Invalid phone number format.")

    @staticmethod
    def validate_age(age):
        """Validate age to be a positive integer."""
        if not isinstance(age, int) or age < 0:
            raise ValidationError("Age must be a positive integer.")

    @staticmethod
    def validate_non_empty_string(value):
        """Validate that a string is not empty."""
        if not isinstance(value, str) or not value.strip():
            raise ValidationError("This field cannot be empty.")
