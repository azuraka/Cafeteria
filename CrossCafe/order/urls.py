from django.conf.urls import include, url
from django.contrib import admin
from . import views

#url goes here which are related to order module
#author rajesh
urlpatterns=[
    url(r'^placeorder',views.placeorder, name='placeorder'),
    url(r'^pay',views.pay, name='pay')
]