from django.db import models


class Restaurant(models.Model):
    r_id = models.IntegerField(default=0,primary_key=True)
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    def __str__(self):
        return self.name+", "+self.city


class FoodItems(models.Model):
    r_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name+"\t"+str(self.price)