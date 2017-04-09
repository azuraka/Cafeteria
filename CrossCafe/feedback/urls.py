from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add', views.addComplaint, name='addComplaint'),
    url(r'^pending', views.showPendingComplaints, name='showComplaint'),
  ]