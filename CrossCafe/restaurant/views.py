from django.shortcuts import render
from django.http import HttpResponse
from restaurant.models import Restaurant
from django.core import serializers

def index(request):
	all_cities = Restaurant.objects.values('city').distinct()
	city_areas = Restaurant.objects.filter(city = all_cities[0]['city']).only('area').distinct()
	city_areas = serializers.serialize('json', list(city_areas), fields=('area'))
	return render(request, 'index.html', {'all_cities': all_cities, 'city_areas': city_areas})

# Handle all cases: If not city, if not area, if not get request
def getAreas(request):
	city = request.GET.get('city')
	city_areas = Restaurant.objects.filter(city = city).only('area').distinct()
	city_areas = serializers.serialize('json', list(city_areas), fields=('area'))
	return HttpResponse(city_areas)