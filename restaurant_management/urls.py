from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^show', views.show_menu, name='index'),
    url(r'^add', views.add_item_to_menu, name='addmenu'),
    url(r'^delete', views.delete_item_from_menu, name='deletemenu'),
     url(r'^disable', views.make_item_unavailable, name='disablemenu'),

]