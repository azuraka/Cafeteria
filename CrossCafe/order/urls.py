from django.conf.urls import include, url
from django.contrib import admin
from . import views

#url goes here which are related to order module
#author rajesh
urlpatterns=[
    url(r'^placeorder',views.placeorder, name='placeorder'),
    url(r'^pay',views.pay, name='pay'),
    url(r'^getcustomerorder',views.get_customer_order, name='get_customer_order'),
    url(r'^getrestaurantorder',views.get_restaurant_order, name='get_restaurant_order'),
]