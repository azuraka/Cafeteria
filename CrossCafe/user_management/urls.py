"""User Management URL Configuration
"""
from django.conf.urls import url
from user_management import views as user_view

urlpatterns = [
    url(r'^$', user_view.index, name='index'),
]