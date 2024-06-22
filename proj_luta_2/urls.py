from django.contrib import admin
from django.urls import path
from app_luta import view 

urlpatterns = [
    path('', view.base,name='base'),
]
