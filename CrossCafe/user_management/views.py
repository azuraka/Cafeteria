from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	return HttpResponse("DB Admin Page")
	#return render(request, 'db_admin_dash.html')
