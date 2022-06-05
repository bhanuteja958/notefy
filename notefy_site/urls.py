import imp
from django import views
from django.urls import path
from . import views

urlpatterns =[
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('', views.home, name='home')
]