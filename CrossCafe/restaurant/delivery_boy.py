from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from restaurant.models import Restaurant
from order.models import Order
from user_management.user_details import UserDetails

def delivery_boys_order(request):
    # getting user id and restaurant from request
    user = UserDetails().getUserType(request)
    all_orders = Order.objects.all().filter(restaurant_id=0,delivery_by=8,status="DISPATCHED")
    print all_orders, len(all_orders)
    return render(request, 'restaurant/orders_to_deliver.html', {'all_orders': all_orders,'user':user})

def deliver_order(request):
    #get userid from request
    #get restaurantid from user table
    order_id = request.GET.get('order_id')
    print order_id
    entry = Order.objects.get(pk=order_id)
    entry.status="DELIVERED"
    entry.save()
    return HttpResponse('<h1>No Orders to deliver</h1>')
