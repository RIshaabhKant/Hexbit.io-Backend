from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('signup/', views.SignUp, name="SignUp"),
    path('signin/', views.Signin, name="SignIn"),
]