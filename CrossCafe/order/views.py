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
from . import OrderDao, ViewUtil,OrderStatus
from django.utils.html import escape

EXTRA_CHARGES = 30;
DELIVERY_CHARGES = 20;

def createOrder(request):
	if request.method == 'POST':
		cart = eval(request.POST['cart'])
		restaurant_id = request.POST['restaurant_id']
		cart_items = []
		total = 0
		for items in cart:
			item_object = FoodItem.objects.get(item_id=items['id'])
			cart_items.append({'item_name': item_object.name, 'item_price': item_object.price})
			total += item_object.price
		grand_total = total + EXTRA_CHARGES + DELIVERY_CHARGES
		new_order = Order(order_items=str(cart_items), status='draft', amount=total, extra_charges=EXTRA_CHARGES, delivery_charges=DELIVERY_CHARGES, restaurant_id=restaurant_id, order_type='online')
		new_order.save()
		print new_order.order_id
		review_page_url = '/order/review'
		return HttpResponseRedirect(review_page_url)
	else:
		return HttpResponseNotFound('<h1>404 Page not found</h1>')

def reviewOrder(request):
    #if request.method == 'GET':
        #raise Http404
    user_id = None
    print "in reviewOrder"
    if 'user_id' in request.session:
        user_id = request.session['user_id']
    else:
        print "in revieworder, no login user found"
        return render(request, 'order/review_order.html', {'cart': None})
    if user_id is None:
        print "user_id is none"
        return render(request, 'order/review_order.html', {'cart': None})
    #If we get user_id in session then save the Order as Draft and navigate to review_order.html page
	cart = Order.objects.filter(status='draft').first()
    print cart
    if(cart):
        return render(request, 'order/review_order.html', {'cart': cart})
    else:
        return render(request, '/')

@csrf_exempt
def placeorder(request):
    customer_id = ViewUtil.ViewUtil.get_customer_id(request)
    order = ViewUtil.ViewUtil.prepare_order(request, customer_id)
    request.session['order_id'] = order.order_id
    order_json = serializers.serialize('json', [ order, ])#serializers.serialize('json', list(order))
    struct = json.loads(order_json)
    order_json = json.dumps(struct[0])
    order_json = json.dumps(json.loads(order_json)['fields'])
    order_json = json.dumps(json.loads(order_json))
    #HttpResponse(order_json)
    return render(request, 'order/review_payment.html', {'order': order})
    #return render(request, 'order/review_payment.html', {'order': order_json})

#Update the payment details in the order table
#Trigger a notification to Attendar for Accept/Reject the order
#Navigate to a page showing Confirmation to customer saying payment successfuly done/pay at your door in case of COD, order is on hold for acceptance
@csrf_exempt
def pay(request):
    order_id = request.session['order_id']#request.POST.get('order_id')
    order_dao = OrderDao.OrderDao.getInstance()
    order = order_dao.find_by_id(order_id)
    if order is not None and order.status != OrderStatus.OrderStatus.DRAFT:
        raise Http404('Order has been already placed and cannot be changed! Please contact our help desk')
    order = ViewUtil.ViewUtil.get_items_from_payment_page(request, order)
    order = order_dao.update(order)
    return render(request, 'order/after_payment.html', {'order': order})
    #return JsonResponse(ViewUtil.ViewUtil.get_payment_json_response(order))

def orderdetails(request):
    #order_id = str(1)
    #orderDao = OrderDao.get_instance()
    #order = orderDao.findById(order_id)
    return render(request, 'order/after_payment.html', {})

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