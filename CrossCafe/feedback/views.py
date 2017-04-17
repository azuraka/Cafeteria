from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import admin
from feedback.models import Complaint
from django.core import serializers
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from restaurant.views import index
from user_management.user_details import UserDetails

admin.site.register(Complaint)
# Create your views here.
  
@csrf_exempt
def addComplaint(request):
    utype = identifyTypeOfUser(request)
    user = UserDetails().getUserType(request)
    # A HTTP POST?
    if request.method == 'POST':
        req = request.POST
        print req
        if utype == 'staff':  status = '0'
        else : status = '1'
        f = Complaint(order_id = int(req['order']), user_type = utype, message = req['message'], status = status)
        f.save()
        # Add success alert notification
        return HttpResponseRedirect('/')

    elif request.method == 'GET':
        order_id = int(request.GET.get('order'))
        prev_complaints = Complaint.objects.filter( order_id = order_id )
        if utype == 'staff':  status = '0'
        elif prev_complaints:
            status = prev_complaints.latest('id').status # status of last complaint
        else :
            status = '0'
        print prev_complaints        
        form = { 'order_id' : order_id }

    return render(request,'feedback/complaintForm.html', {'form': form, 'complaints': prev_complaints, 'status': status, 'user':user})

def showPendingComplaints(request):
    user = UserDetails().getUserType(request)
    orders = Complaint.objects.all().values_list('order_id', flat=True).distinct()
    complaints = []
    for entry in orders:
        entry = Complaint.objects.filter(order_id = entry).latest('id')
        if entry.status == '1':
            complaints.append(entry)

    return render(request,'feedback/pendingComplaint.html', {'complaints': complaints,'user':user})



def identifyTypeOfUser(request):
    if request.method == 'GET':
        order_id = int(request.GET.get('order'))
    else :
        order_id = int(request.POST['order'])

    if isManagerForOrder(request.user,order_id):   
        utype = 'staff'
    else :
        utype = 'customer'  
    return utype


def isManagerForOrder(user,order):
    # if user is manager of the same retaurant as the order
    # return yes
    # else no
    return 1

