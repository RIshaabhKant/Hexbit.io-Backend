from django.urls import path

from shipper import views


urlpatterns = [
    path('create/', views.createShipper, name='createShipper'),
    path('view/<int:pk>', views.getShipper, name='getShipper'),
    path('update/<int:pk>', views.updateShipper, name='updateShipper'),
]