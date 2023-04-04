from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name="SignUp"),
    path('signin/', views.Signin, name="SignIn"),
    path('access/', views.getAccess, name="GetAccessToken"),
]