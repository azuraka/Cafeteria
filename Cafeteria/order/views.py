from django.shortcuts import render

# Create your views here.

def placeorder(request):
    pass
    #update the order first into DB
    #navigate to payment page

def pay(request, order):
    pass
    #Update the payment details in the order table
    #Trigger a notification to Attendar for Accept/Reject the order
    #Navigate to a page showing Confirmation to customer saying payment successfuly done/pay at your door in case of COD, order is on hold for acceptance