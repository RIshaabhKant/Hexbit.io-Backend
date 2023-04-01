from django.urls import path

from product import views


urlpatterns = [
    path('view/', views.getProducts, name='getProducts'),
    path('create/', views.postProducts, name='postProducts'),
    path('update/<int:pk>', views.updateProduct, name='updateProducts'),
    path('delete/', views.deleteProducts, name='deleteProducts'),
]