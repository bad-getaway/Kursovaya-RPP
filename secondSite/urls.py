from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home2'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('game/<int:pk>', views.game, name='game'),
    path('admingame/<int:pk>', views.admingame, name='admingame'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
