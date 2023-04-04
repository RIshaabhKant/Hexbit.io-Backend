from django.urls import path

from order_details import views


urlpatterns = [
    path('view/<int:pk>', views.getOrders, name='getOrders'),
    path('update/', views.updateOrders, name='updateOrders')
]