from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from restaurant.models import Restaurant
from django.core import serializers
from user_management.models import UserProfile
from user_management.user_details import UserDetails

# if-else vs. try-except
def index(request):
    user = UserDetails().getUserType(request)
    all_cities = Restaurant.objects.values('city').distinct()
    city_areas = Restaurant.objects.filter(city=all_cities[0]['city']).only('area').distinct()
    if(city_areas):
        city_areas = serializers.serialize('json', list(city_areas), fields=('area'))
        return render(request, 'index.html', {'all_cities': all_cities, 'city_areas': city_areas, 'user' : user})
    else:
        return HttpResponse('<h1>Restaurant not available in your city</h1>')


# Handle different case types (uppercase, lowercase, etc)
def getAreas(request):
    if(request.GET.get('city')):
        city = request.GET.get('city')
        city_areas = Restaurant.objects.filter(city=city).only('area').distinct()
        if(city_areas):
            city_areas = serializers.serialize('json', list(city_areas), fields=('area'))
            return HttpResponse(city_areas)
        else:
            return HttpResponse('<h1>Restaurant not available in your city</h1>')
    else:
        home_page_url = '/'
    return HttpResponseRedirect(home_page_url)