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
		cart_items = []
		total = 0
		for items in cart:
			item_object = FoodItem.objects.get(item_id=items['id'])
			cart_items.append({'item_name': item_object.name, 'item_price': item_object.price})
			total += item_object.price
		#print cart_items
		grand_total = total + EXTRA_CHARGES + DELIVERY_CHARGES
		new_order = Order(order_items=str(cart_items), status='draft', amount=total, extra_charges=EXTRA_CHARGES, delivery_charges = DELIVERY_CHARGES, order_type='online')
		new_order.save()
		print new_order.order_id
		return HttpResponse('Order created sucessfully')
	else:
		return HttpResponseNotFound('<h1>404 Page not found</h1>')

def showOrder(request):
	print request.GET.get('order_id')
	return HttpResponse('temp')