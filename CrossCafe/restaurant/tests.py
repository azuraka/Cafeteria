from django.test import TestCase
from restaurant.models import Restaurant
import requests

# Create your tests here.
class APITesting(TestCase):
	def test_index(self):
		request_url = "http://127.0.0.1:8065/"
		response = requests.get(request_url)
		self.assertIsNotNone(response)
		self.assertEqual(response.status_code, 200, "home page not loading")

	def test_getAreas(self):
		request_url = "http://127.0.0.1:8065/?city=Hyderabad"
		response = requests.get(request_url)
		self.assertIsNotNone(response)
		self.assertEqual(response.status_code, 200, "cannot get areas")

		request_url = "http://127.0.0.1:8065/?city=Chennai"	# no restaurant in city
		response = requests.get(request_url)
		self.assertIsNotNone(response)
		self.assertEqual(response.status_code, 200, "cannot get areas")




