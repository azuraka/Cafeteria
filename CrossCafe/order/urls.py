"""Order URL Configuration
"""
from django.conf.urls import url
from order import views

urlpatterns = [
	url(r'^create', views.createOrder, name='createOrder'),
    url(r'^show', views.showOrder, name='showOrder'),
]