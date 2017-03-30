"""Order URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from order import views

urlpatterns = [
	url(r'^create', views.createOrder, name='createOrder'),
    url(r'^review', views.reviewOrder, name='reviewOrder'),
	url(r'^placeorder',views.placeorder, name='placeorder'),
    url(r'^pay',views.pay, name='pay'),
    url(r'^getcustomerorder',views.get_customer_order, name='get_customer_order'),
    url(r'^getrestaurantorder',views.get_restaurant_order, name='get_restaurant_order'),
]