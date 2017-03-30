"""Manage Order
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from order.models import Order
from menu.models import FoodItem

EXTRA_CHARGES = 30;
DELIVERY_CHARGES = 20;

def createOrder(request):
	if request.method == 'POST':
		cart = eval(request.POST['cart'])
		restaurant_id = request.POST['restaurant_id']
		cart_items = []
		total = 0
		for items in cart:
			item_object = FoodItem.objects.get(item_id=items['id'])
			cart_items.append({'item_name': item_object.name, 'item_price': item_object.price})
			total += item_object.price
		grand_total = total + EXTRA_CHARGES + DELIVERY_CHARGES
		new_order = Order(order_items=str(cart_items), status='draft', amount=total, extra_charges=EXTRA_CHARGES, delivery_charges=DELIVERY_CHARGES, restaurant_id=restaurant_id, order_type='online')
		new_order.save()
		print new_order.order_id
		review_page_url = '/order/review'
		return HttpResponseRedirect(review_page_url)
	else:
		return HttpResponseNotFound('<h1>404 Page not found</h1>')

def reviewOrder(request):
	cart = Order.objects.filter(status='draft')
	if(cart):
		return render(request, 'order/review_order.html', {'cart': cart})
	else:
		return render(request, 'order/review_order.html')