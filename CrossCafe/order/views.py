from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core import serializers
import json
from .models import Order
from . import OrderDao, ViewUtil
# Create your views here.

#update the order first into DB
#navigate to payment page
@csrf_exempt
def placeorder(request):
    order_id = request.POST.get('order_id')
    order_dao = OrderDao.OrderDao.getInstance()
    order = order_dao.find_by_id(order_id)
    order = ViewUtil.ViewUtil.get_items_from_placeorder_page(request, order)
    order = order_dao.update(order)
    return HttpResponse(serializers.serialize('json', [order, ]))

#Update the payment details in the order table
#Trigger a notification to Attendar for Accept/Reject the order
#Navigate to a page showing Confirmation to customer saying payment successfuly done/pay at your door in case of COD, order is on hold for acceptance
@csrf_exempt
def pay(request):
    order_id = request.POST.get('order_id')
    order_dao = OrderDao.OrderDao.getInstance()
    order = order_dao.find_by_id(order_id)
    order = ViewUtil.ViewUtil.get_items_from_payment_page(request, order)
    order = order_dao.update(order)
    return JsonResponse(ViewUtil.ViewUtil.get_payment_json_response(request, order))

def orderdetails(request):
    #order_id = str(1)
    #orderDao = OrderDao.get_instance()
    #order = orderDao.findById(order_id)

    return render(request, 'order/orderdetails.html', {})

@csrf_exempt
def get_customer_order(request):
    if not request.method == 'POST':
        raise Http404("Invalid Request")
    customer_id = request.POST.get('customer_id')
    order = OrderDao.OrderDao.getInstance().find_by_customer_id(customer_id)
    if order is None:
        order = '{}'
    return HttpResponse(serializers.serialize('json', order))

@csrf_exempt
def get_restaurant_order(request):
    if not request.method=='POST':
        raise Http404("Invalid Request")
    restaurant_id = request.POST.get('restaurant_id')
    order = OrderDao.OrderDao.getInstance().find_by_restaurant_id(restaurant_id)
    if order is None:
        order = '{}'
    #result = [{'order': o.area} for r in allAreas]
    orders = serializers.serialize('json', list(order))
    return HttpResponse(orders)