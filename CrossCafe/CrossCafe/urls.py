"""CrossCafe URL Configuration
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from restaurant import views as restaurant_view


urlpatterns = [
    url(r'^$', restaurant_view.index, name='index'),
    url(r'^restaurant/', include('restaurant.urls')),
    url(r'^menu/', include('menu.urls')),
    url(r'^order/', include('order.urls')),
    url(r'^complaint/', include('feedback.urls')),
    url(r'^user/', include('user_management.urls')),
    url(r'^cas/', include('cas_server.urls', namespace="cas_server")),
    
    url(r'^admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
