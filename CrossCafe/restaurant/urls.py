"""Restaurant URL Configuration
"""
from django.conf.urls import url
from restaurant import views, attendant, delivery_boy, search_restaurant

urlpatterns = [
    url(r'^gps_search', search_restaurant.gpsSearch, name='gpsSearch'),
    url(r'^dropdown_search', search_restaurant.dropdownSearch, name='dropdownSearch'),
    url(r'^get_areas', views.getAreas, name='getAreas'),
    url(r'^get_waiting_orders', attendant.get_all_waiting_orders, name='waitingOrders'),

    url(r'^approve_order', attendant.approve_order, name='approveOrder'),
    url(r'^decline_order', attendant.decline_order, name='declineOrder'),
    
    url(r'^get_accepted_orders', attendant.get_all_accepted_orders, name='acceptedOrders'),
	url(r'^assign_delivery_boy', attendant.assign_delivery_boy, name='assignDboy'),
	url(r'^get_orders_to_deliver', delivery_boy.delivery_boys_order, name='getOrdersToDeliver'),
	url(r'^deliver_the_order', delivery_boy.deliver_order, name='deliverOrder'),    
]