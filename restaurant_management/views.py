from django.shortcuts import render
from restaurant_management.models import Restaurant,FoodItems
from django.http import HttpResponse

# Create your views here.
def show_menu(request):
    # get restaurant name from request
    restaurant_name = request.GET.get("rname","0")
    r = Restaurant.objects.get(name__iexact=restaurant_name)
    #print r.exists(restaurant_name)
    menu = FoodItems.objects.filter(r_id = r,status = True)
    menu = [{'name':m.name,'price':str(m.price)} for m in menu]

    #return a list
    return HttpResponse(str(menu))

def add_item_to_menu(request):
    restaurant_name = request.GET.get("rname","0")
    item_name = request.GET.get("iname","0")
    price = request.GET.get("price",0)
    r = Restaurant.objects.get(name__iexact=restaurant_name)
    f = FoodItems.objects.filter(name=item_name)
    if not f.exists():
        f = FoodItems(r_id = r, name = item_name, price = price )
        f.save()
        return HttpResponse("Done adding "+item_name+" to "+restaurant_name)
    else :
        f=f[0]
        f.price= price
        f.save()
        return HttpResponse("Item Updated")

def delete_item_from_menu(request):
    restaurant_name = request.GET.get("rname","0")
    r = Restaurant.objects.get(name__iexact=restaurant_name)
    item_name = request.GET.get("iname","0")
    FoodItems.objects.filter(r_id=r,name=item_name).delete()
    return HttpResponse("Done deleting"+item_name+"from "+restaurant_name)

def make_item_unavailable(request):
    restaurant_name = request.GET.get("rname","0")
    r = Restaurant.objects.get(name__iexact=restaurant_name)
    item_name = request.GET.get("iname","0")
    f = FoodItems.objects.get(r_id=r, name=item_name)
    f.status = False
    f.save()
    return show_menu(request)





