from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),

    path('catalog/', views.catalog, name='catalog'),
    path('choose_category/<int:pk>', views.choose_category, name='choose_category'),
    path('choose_product/<int:pk>', views.choose_product, name='choose_product'),
    path('make_order/<int:pk>', views.make_order, name='make_order'),
    path('game_pass/', views.game_pass, name='game_pass'),

    path('api/v1/order_all', views.OrderListView.as_view()),
    path('api/v1/game_all', views.GameListView.as_view()),
    path('api/v1/category_all', views.CategoryListView.as_view()),


    path('login_page/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
