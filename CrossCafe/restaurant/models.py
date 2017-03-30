from __future__ import unicode_literals

from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.IntegerField(default=0,primary_key=True)
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    
    def __str__(self):
    	return '%s, %s, %s' % (self.name, self.area, self.city)
