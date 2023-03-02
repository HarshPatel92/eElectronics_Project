from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('index/', views.index),
    path('login',views.login),
    path('aboutus/',views.aboutUs),
    path('contactus/',views.contactUs),
    path('feedback/',views.feedback),
    
]
