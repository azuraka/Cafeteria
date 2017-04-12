from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from restaurant.models import Restaurant
from django.core import serializers
from CrossCafe.order.models import Order

