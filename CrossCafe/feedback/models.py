from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
import datetime
# Create your models here.
class Complaint(models.Model):
    order_id = models.IntegerField(default=0)
    user_type_choice = (('c','customer'),('s','staff'))
    user_type = models.CharField(max_length=100,choices=user_type_choice,default='customer') #choices = {'customer','staff'}
    message = models.CharField(max_length=500)
    date = models.DateField(default=datetime.date.today)
    complaint_status_choice = (('1','pending'),('0','closed'))
    status = models.CharField(max_length=50,choices=complaint_status_choice)
    
    def __str__(self):
       return str(self.order_id)+self.message+"\t"+str(self.status)