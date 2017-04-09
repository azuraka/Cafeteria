"""Manage Order
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import Http404, JsonResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core import serializers
import json
from order.models import Order
from menu.models import FoodItem
from . import OrderDao, ViewUtil


def viewPreviousOrder(request):
    order_id = request.GET.get("orderID",0)
    #if request.user.type == "manager" :
    o = OrderDao.OrderDao()
    order = o.find_by_id(order_id)
    print order
    return render(request, 'order/vieworder.html', {'order':order})
