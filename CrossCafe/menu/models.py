from __future__ import unicode_literals

from django.db import models
from restaurant.models import Restaurant

class FoodItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '%s\t%s' % (self.name, self.price)
