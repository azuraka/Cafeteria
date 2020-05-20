from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^show', views.show_menu, name='index'),
    url(r'^add', views.add_item_to_menu, name='addmenu'),
    url(r'^delete', views.delete_item_from_menu, name='deletemenu'),
    url(r'^disable', views.make_item_unavailable, name='disablemenu'),
    url(r'^getareas', views.get_areas, name='getareas'),
    url(r'^getcities', views.get_all_cities, name='getcities'),
    url(r'^getrestaurant', views.get_restaurant, name='getrestaurant'),
]