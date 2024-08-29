import json
from requests import status_codes
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
import os.path

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

    def test_get_bullish_engullfing(self):
        response = client.get(reverse('api.bullish_engullfing'))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_doji(self):
        response = client.get(reverse('api.doji'))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_falling_wedge(self):
        response = client.get(reverse('api.falling_wedge'))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_rising_wedge(self):
        response = client.get(reverse('api.rising_wedge'))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_hammer(self):
        response = client.get(reverse('api.hammer'))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_near_52week_high(self):
        response = client.get(reverse('api.near_52week_high'))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_near_52week_low(self):
        response = client.get(reverse('api.near_52week_low'))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_is_symbol_forms_hammer(self):
        symbol = 'RELIANCE'
        response = client.get(reverse(viewname='api.hammer.symbol', kwargs={'symbol': symbol}))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_watchlist(self):
        symbol = 'RELIANCE'
        response = client.get(reverse(viewname='api.watchlist.add', kwargs={'symbol': symbol}))
        self.assertTrue(os.path.isfile('api/data/watchlist.txt'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(reverse(viewname='api.watchlist.get'))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_has_watchlist(self):
        symbol = 'RELIANCE'
        response = client.get(reverse(viewname='api.watchlist.add', kwargs={'symbol': symbol}))
        self.assertTrue(os.path.isfile('api/data/watchlist.txt'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(reverse(viewname='api.watchlist.has', kwargs={'symbol': symbol}))
        response_data = json.loads(response.content)
        self.assertTrue('data' in response_data and response_data['data'] == True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_add_to_watchlist(self):
        symbol = 'RELIANCE'
        response = client.get(reverse(viewname='api.watchlist.add', kwargs={'symbol': symbol}))
        self.assertTrue(os.path.isfile('api/data/watchlist.txt'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remove_from_watchlist(self):
        symbol = 'RELIANCE'
        response = client.get(reverse(viewname='api.watchlist.remove', kwargs={'symbol': symbol}))
        self.assertTrue(os.path.isfile('api/data/watchlist.txt'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
                    
    def clear_watchlist(self):
        symbol = 'RELIANCE'
        response = client.get(reverse(viewname='api.watchlist.clear'))
        self.assertTrue(os.path.isfile('api/data/watchlist.txt') == False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
