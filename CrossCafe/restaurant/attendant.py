from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from restaurant.models import Restaurant
from order.models import Order


def get_all_waiting_orders(request):
    print 
    #get userid from request
    #get restaurantid from user table
    restaurant_id=0
    status="AWAITING_ACCEPTANCE"
    all_waiting_orders = get_orders(restaurant_id,status)
    # user_details = Auth.ojects.all().filter(id=)
    # -------------get user details (name + phone no) from user table-------------    
    print len(all_waiting_orders)
    print all_waiting_orders
    return render(request, 'restaurant/pending_orders.html', {'all_waiting_orders': all_waiting_orders})
    
def get_all_accepted_orders(request):
    #get userid from request
    #get restaurantid from user table
    restaurant_id=0
    status="ACCEPTED"
    all_accepted_orders = get_orders(restaurant_id,status)
    # all_available_delivery_boys
    # user_details =-------------get user details (name + phone no) from user table-------------
    print all_accepted_orders
    return render(request, 'restaurant/accepted_orders.html', {'all_accepted_orders': all_accepted_orders, 'available_boys' :all_accepted_orders })
    
def get_orders(restaurant_id,status):

    all_orders=Order.objects.all().filter(restaurant_id=restaurant_id,status=status)
    return all_orders

def assign_delivery_boy(request):
    order_id = request.GET.get('order_id')
    delivery_boy_id = request.GET.get('delivery_boy_id')
    print order_id, delivery_boy_id
    
    #Send notification to delivery boy

    #saving it in DB
    # entry = Order.objects.get(pk=order_id)
    # entry.delivery_by=delivery_boy_id
    # entry.status="DISPATCHED"
    # entry.save()
    return HttpResponse("")

def approve_order(request):
    #get userid from request
    #get restaurantid from user table
    order_id = request.GET.get('order_id')
    print order_id
    entry = Order.objects.get(pk=order_id)
    entry.status="ACCEPTED"
    entry.save()
    return HttpResponse('<h1>No Pending Orders</h1>')

def decline_order(request):
    #get userid from request
    #get restaurantid from user table
    order_id = request.GET.get('order_id')
    print order_id
    entry = Order.objects.get(pk=order_id)
    entry.status="DECLINED"
    entry.save()
    return HttpResponse('<h1>No Pending Orders</h1>')
