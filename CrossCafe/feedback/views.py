from django.shortcuts import render
from django.http import HttpResponse
from feedback.models import Complaint,ComplaintForm
from django.core import serializers
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def showComplaintStatus(request):
    order_id = request.GET.get("orderID",0)
    if order_id :
        return HttpResponse(str(Complaint.objects.filter(order_id = order_id)[0].status))
    else :
        return HttpResponse(str("no Complaints found for the following orderId"))
    

def addComplaint(request):
    context = RequestContext(request)
    # A HTTP POST?
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ComplaintForm()
    return render_to_response('feedback/complaintForm.html', {'form': form}, context)

def change_status_of_complaint(orderID,status):
    c = Complaint.objects.get(order_id = orderID)
    c.status = status
    c.save()

def showPendingComplaints(request):
    c = Complaint.objects.filter(status='pending')
    c = serializers.serialize('json', list(c))
    return HttpResponse(str(c))


def validRequest(request):
    pass


