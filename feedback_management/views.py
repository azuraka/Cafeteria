from django.shortcuts import render
from django.http import HttpResponse
from feedback_management.models import Feedback

# Create your views here.
def show_complaint_status(request):
