"""Manage Menu
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from menu.models import FoodItem
from restaurant.models import Restaurant


def showMenu(request):
    if(request.GET.get('restaurant_id')):
        restaurant_id = request.GET.get('restaurant_id')
        menu = FoodItem.objects.filter(restaurant_id=restaurant_id, status=True)
        print menu
        return render(request, 'menu/show_menu.html', {'menu': menu})
    else:
        home_page_url = '/'
        return HttpResponseRedirect(home_page_url)

def add_item_to_menu(request):
		#try:
	    r_id = request.GET.get("restaurant_id",0)
	    item_name = request.GET.get("iname","0")
	    price = request.GET.get("price",0)
	    r = Restaurant.objects.get(restaurant_id=r_id)
	    f = FoodItem.objects.filter(restaurant_id = r, name=item_name)
	    if not f.exists():
	        f = FoodItem(restaurant_id = r, name = item_name, price = price )
	        f.save()
	        return HttpResponse("Done adding "+item_name+" to "+r.name)
	    else :
	        f=f[0]
	        f.price= price
	        f.save()
	        return HttpResponse("Item Updated")
		#except :
		return HttpResponse("Error")