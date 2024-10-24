import unittest
from services.analytics import AnalyticsService
from database import session
from patient import Patient

class TestAnalyticsService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = AnalyticsService(db_session=session)

    def test_get_patient_statistics(self):
        # Add test data
        session.add(Patient(name="Alice", age=25, email="alice@example.com"))
        session.add(Patient(name="Bob", age=30, email="bob@example.com"))
        session.commit()

        stats = self.service.get_patient_statistics()
        self.assertEqual(stats['total_patients'], 2)
        self.assertAlmostEqual(stats['average_age'], 27.5)

    def test_get_provider_statistics(self):
        # Assuming Provider model and data exist
        stats = self.service.get_provider_statistics()
        self.assertIsNotNone(stats)

if __name__ == '__main__':
    unittest.main()
