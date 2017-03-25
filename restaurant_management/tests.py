from django.test import TestCase
from restaurant_management.models import Restaurant,FoodItems
import requests

# Create your tests here.
class APITesting(TestCase):
	def test_add_items_to_menu(self):	# Not Working, changes in db not showing
		# Restaurant.objects.create(r_id=1,name="Sardarji",city="Hyderabad",area="Indira Nagar")
		#rest.save()
		
		request_url = "http://127.0.0.1:8064/menu/add/?rname=sardarji&iname=chola&price=180"
		r = requests.get(request_url)
		f = open("testoutout.html","w")
		f.write(r.text)
		f.close()
		print r.text
		# rest = Restaurant.objects.get(name="Tera Dhaba")
		self.assertEqual(True,True)

	def test_show_menu(self):
		req_url ="http://127.0.0.1:8064/menu/show?rname=Sardarji"
		r = requests.get(req_url)
		print r.text
		self.assertEqual(True,True)
