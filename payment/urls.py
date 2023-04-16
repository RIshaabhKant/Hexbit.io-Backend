from django.urls import path

from payment import views


urlpatterns = [
    path('view/<int:pk>', views.getPayments, name='getPayments'),
]