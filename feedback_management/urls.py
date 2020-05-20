from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^status', views.show_complaint_status, name='complaintStatus'),
    url(r'^add', views.add_complaint, name='addComplaint'),
    url(r'^pending', views.show_pending_compalints, name='showComplaint'),
  ]