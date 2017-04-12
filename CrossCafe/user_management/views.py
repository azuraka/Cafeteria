from django.shortcuts import render
from user_management.models import UserProfile
from order.models import Order
from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import Http404, JsonResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core import serializers

#admin.site.register(User)
# Create your views here.

def viewOrderHistory(request):
    start_index = request.session.get('index',0)
    #print UserProfile.objects.get(user=request.user).user_type
    # username = None
    # if request.user.is_authenticated():
    #     username = request.user.user_id
    user_id = "rajesh@gmail.com"
    try:
        orders = Order.objects.filter(customer_id = user_id)[:7]
    except:
        orders = []
    #request.session['index'] = start_index+10
    # print orders[0]
    
    return render(request, 'order/myorders.html', {'order': orders})