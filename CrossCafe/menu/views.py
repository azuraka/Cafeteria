"""Manage Menu
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from menu.models import FoodItem


def showMenu(request):
    if(request.GET.get('restaurant_id')):
        restaurant_id = request.GET.get('restaurant_id')
        menu = FoodItem.objects.filter(restaurant_id=restaurant_id, status=True)
        return render(request, 'menu/show_menu.html', {'menu': menu})
    else:
        home_page_url = '/'
        return HttpResponseRedirect(home_page_url)
