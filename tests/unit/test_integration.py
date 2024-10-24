import unittest
from services.integration import IntegrationService
from database import session
from patient import Patient

class TestIntegrationService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = IntegrationService(db_url='sqlite:///:memory:')  # Use in-memory database for testing
        cls.service.session = session

    def test_integrate_patient_data(self):
        patient_data = {
            "name": "John Doe",
            "age": 30,
            "email": "john.doe@example.com"
        }
        patient = self.service.integrate_patient_data(patient_data)
        self.assertIsNotNone(patient)
        self.assertEqual(patient.name, "John Doe")

    def test_integrate_invalid_patient_data(self):
        invalid_data = {
            "name": "",  # Invalid name
            "age": -1,   # Invalid age
            "email": "invalid_email"
        }
        patient = self.service.integrate_patient_data(invalid_data)
        self.assertIsNone(patient)

if __name__ == '__main__':
    unittest.main()
