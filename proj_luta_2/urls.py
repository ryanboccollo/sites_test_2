from django.contrib import admin
from django.urls import path
from app_luta import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('index/organizador', views.organizador, name='organizador'),
    path('index/academia', views.academia, name='academia'), 


]
