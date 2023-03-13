from django.contrib import admin
from django.urls import path,include
from .views import ManagerRegisterView,DeveloperRegisterView

urlpatterns = [
    path('managerregister/',ManagerRegisterView.as_view(),name='managerregister'),
    path('developerregister/',DeveloperRegisterView.as_view(),name='developerregister')
]
