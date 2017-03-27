"""Manage Order
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from menu.models import FoodItem

def createOrder(request):
	if request.method == 'POST':
		cart = request.POST['cart'].split()
		return HttpResponse('Order created sucessfully')
	else:
		return HttpResponseNotFound('<h1>404 Page not found</h1>')

def showOrder(request):
	return HttpResponse('temp')