from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^status', views.showComplaintStatus, name='complaintStatus'),
    url(r'^add', views.addComplaint, name='addComplaint'),
    url(r'^pending', views.showPendingComplaints, name='showComplaint'),
  ]