from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
from user.models import User
from .models import GlucoseLevel

# Create your tests here.

class GlucoseLevelTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='marline', password='password')
        
        self.glucose_level = GlucoseLevel.objects.create(
            user=self.user,
            timestamp=datetime.now(),
            glucose_value=120
        )
        self.glucose_level_url = reverse('glucose-level-detail', kwargs={'pk': self.glucose_level.id})
        self.glucose_level_list_url = reverse('glucose-level-list')
        self.glucose_level_create_url = reverse('glucose-level-create')
        
    def test_create_glucose_level(self):
        data = {
            'user': self.user.id,
            'timestamp': '2024-07-24T10:00:00Z',
            'glucose_value': 130
        }
        response = self.client.post(self.glucose_level_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GlucoseLevel.objects.count(), 2)
        self.assertEqual(GlucoseLevel.objects.latest('id').glucose_value, 130)
        
    def test_list_glucose_levels(self):
        response = self.client.get(self.glucose_level_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

    def test_retrieve_glucose_level(self):
        response = self.client.get(self.glucose_level_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['glucose_value'], 120)

    