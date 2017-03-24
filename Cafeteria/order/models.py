from __future__ import unicode_literals

from django.db import models
import datetime

# It represents the Order
# author : rajesh
class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    orderName = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    amount = models.DecimalField()
    extraCharges = models.DecimalField()
    deliveryCharges = models.DecimalField()
    customerId = models.CharField(max_length=100)
    restaurantId = models.CharField()
    deliveryAddress = models.CharField(max_length=2000)
    paymentType = models.CharField() #This represents the type of payment(COD/CreditCard/DebitCard/NetBanking/Cash)
    orderType = models.CharField() #This represents the type of Order - online(customer orders through webapp)/Offline - in Cafeteria
    billDate = models.DateTimeField(blank=True) #The datetime when the order is confirmed from customer(after success payment or COD page confirmation)
    deliveryBy = models.CharField() #It stores take away or the delivery boy name
    lastUpdateBy = models.CharField()
    lastUpdateDate = models.DateTimeField(default=datetime.now, blank=False)
