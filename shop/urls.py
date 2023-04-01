
from django.urls import path

from shop import views


urlpatterns = [
    path('view/', views.getShops, name='getShops'),
    path('create/', views.createShop, name='createShop'),
    path('update/<int:pk>', views.updateShop, name='updateShop'),
    path('delete/', views.deleteShops, name='deleteShops'),
]