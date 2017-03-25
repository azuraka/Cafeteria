from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Feedback(models.Model):
    order_id = models.IntegerField(default=0)
    message = models.CharField(max_length=500)
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.order_id+", "+self.status
