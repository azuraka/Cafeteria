from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# It represents the Order
# author : rajesh


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_name = models.CharField(max_length=500, blank=True, null=True)
    order_items = models.CharField(max_length=5000, blank=True, null=True)
    status = models.CharField(max_length=20)
    amount = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    extra_charges = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    delivery_charges = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    restaurant_id = models.CharField(max_length=1000)
    delivery_address = models.CharField(max_length=2000, blank=True, null=True)
    payment_type = models.CharField(max_length=50, blank=True, null=True) #This represents the type of payment(COD/CreditCard/DebitCard/NetBanking/Cash)
    order_type = models.CharField(max_length=10) #This represents the type of Order - online(customer orders through webapp)/Offline - in Cafeteria
    bill_date = models.DateTimeField(blank=True, null=True) #The datetime when the order is confirmed from customer(after success payment or COD page confirmation)from
    delivery_by = models.CharField(max_length=100, blank=True, null=True) #It stores take away or the delivery boy name
    last_update_by = models.CharField(max_length=100)
    last_update_date = models.DateTimeField(default=datetime.now, blank=False)
    is_deleted = models.BooleanField(default=False)#To support the soft delete feature for any order information

    def __str__(self):
        return '%s-%s-%s' % (self.order_id, self.order_name, self.status)
