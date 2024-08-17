import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings

# initialize the APIClient app
client = Client()

class AllControllersTest(TestCase):
    """ Test module for GET all dashboard APIs """

    def setUp(self):
        pass

    def test_get_api_version(self):
        response = client.get(reverse('api.version'))
        response_data = json.loads(response.content)
        self.assertEqual(response_data['version'], settings.API_VERSION)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_oi_gainers(self):
        response = client.get(reverse('api.oi_gainers'))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_oi_losers(self):
        response = client.get(reverse('api.oi_losers'))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)