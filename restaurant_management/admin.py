from django.contrib import admin

# Register your models here.
from .models import Restaurant,FoodItems

admin.site.register(Restaurant)
admin.site.register(FoodItems)