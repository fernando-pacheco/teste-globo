from django.test import TestCase
from .models import ProgramAudience, InventoryAvailability

class ProgramDataTest(TestCase):
    def setUp(self):
        ProgramAudience.objects.create(signal='signal1', program_code='program1', exhibition_date='2023-07-01', program_start_time='20:00', average_audience=10.0)
        InventoryAvailability.objects.create(signal='signal1', program_code='program1', date='2023-07-01', available_time=100)

    def test_get_program_data(self):
        response = self.client.get('/api/program/program1/2023-07-01/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['available_time'], 100)
        self.assertEqual(response.json()['predicted_audience'], 10.0)

    def test_get_period_data(self):
        response = self.client.get('/api/period/2023-06-01/2023-07-01/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['available_time'], 100)
        self.assertEqual(response.json()[0]['predicted_audience'], 10.0)
