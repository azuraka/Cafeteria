"""Menu URL Configuration
"""
from django.conf.urls import url
from menu import views

urlpatterns = [
    url(r'^show', views.showMenu, name='showMenu'),
]