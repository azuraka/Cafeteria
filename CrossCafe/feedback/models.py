from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

# Create your models here.
class Complaint(models.Model):
    #order_id = models.ForeignKey(default=0)
    order_id = models.IntegerField(default=0)
    message = models.CharField(max_length=500)
    
    complaint_status_choice = (('1','pending'),('0','closed'))
    status = models.CharField(max_length=50,choices=complaint_status_choice)
    
    def __str__(self):
       return self.message+"\t"+str(self.status)

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['order_id','message']
