"""Search the nearest restaurant branch within limited radius
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from restaurant.models import Restaurant


def gpsSearch(request):
    return HttpResponse('Success')


def dropdownSearch(request):
    if request.method == 'POST':
        city = request.POST['city']
        area = request.POST['area']
        try:
            restaurant_id = Restaurant.objects.get(city=city, area=area).restaurant_id
            menu_page_url = '/menu/show/?restaurant_id=' + str(restaurant_id)
            return HttpResponseRedirect(menu_page_url)
        except ObjectDoesNotExist:
            return HttpResponse('<h1>Restaurant not available in your area</h1>')
    else:
        return HttpResponseNotFound('<h1>404 Page not found</h1>')
