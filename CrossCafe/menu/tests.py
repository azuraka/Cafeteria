from django.test import TestCase
from django.http import HttpResponse, HttpResponseRedirect
from menu.models import FoodItem
# Create your tests here.
from django.test import TestCase
from restaurant.models import Restaurant
import requests

# Create your tests here.
class APITesting(TestCase):
	def test_add_items_to_menu(self):	# Not Working, changes in db not showing
		request_url = "http://127.0.0.1:8065/menu/add?restaurant_id=0&iname=paneerchilli&price=200"
		response = requests.get(request_url)
		self.assertIsNotNone(response)
		self.assertEqual(response.content, "Item Updated", "adding item failed")
		self.assertEqual(response.status_code, 200, "add item to menu API failed")

		request_url = "http://127.0.0.1:8065/menu/add?restaurant_id=0&iname=chola&price=160"
		response = requests.get(request_url)
		self.assertIsNotNone(response)
		print response.content
		self.assertEqual(response.content[:5], "Done ", "adding item failed")
		self.assertEqual(response.status_code, 200, "add item to menu API failed")



	def test_show_menu(self):
		req_url ="http://127.0.0.1:8065/menu/show?restaurant_id=0"
		response = requests.get(req_url)
		self.assertIsNotNone(response)
		self.assertEqual(response.status_code, 200, "show menu API failed")

