from django.test import TestCase
from restaurant_management.models import Restaurant,FoodItems


# Create your tests here.
def test_add_items_to_menu():
	request = "http://127.0.0.1:8064/menu/add/?rname=Tera Dhaba&iname=Manchurian&price=180"
	assert(FoodItems.objects.get(name=item_name).price)

