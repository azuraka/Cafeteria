from django.shortcuts import render
from django.http import HttpResponse
from feedback_management.models import Complaint
from django.core import serializers

# Create your views here.
def show_complaint_status(request):
    order_id = request.GET.get("oid","0")
    try:
        return HttpResponse(str(Complaint.objects.filter(order_id = order_id)[0].status))
    except:
        return HttpResponse(str("no Complaints found for the following orderId"))
    

def add_complaint(request):
    order_id = request.GET.get("oid","0")
    message = "default complaint!"
    status = 'pending'
    c = Complaint(order_id=order_id,message=message,status=status)
    c.save()
    return HttpResponse(str("Complaint Placed"))

def change_status_of_complaint(orderID,status):
    c = Complaint.objects.get(order_id = orderID)
    c.status = status
    c.save()

def show_pending_compalints(request):
    c = Complaint.objects.filter(status='pending')
    c = serializers.serialize('json', list(c))
    return HttpResponse(str(c))



