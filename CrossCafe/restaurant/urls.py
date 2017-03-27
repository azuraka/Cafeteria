"""Restaurant URL Configuration
"""
from django.conf.urls import url
from restaurant import search_restaurant

urlpatterns = [
    url(r'^gps_search', search_restaurant.gpsSearch, name='gpsSearch'),
    url(r'^dropdown_search', search_restaurant.dropdownSearch, name='dropdownSearch'),
]