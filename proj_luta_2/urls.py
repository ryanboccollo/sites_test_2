from django.contrib import admin
from django.urls import path
from app_luta import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('index/organizador', views.organizador, name='organizador'),
    path('index/academia', views.academia, name='academia'), 
    path('academia/cadastro_academia', views.cadastro_academia, name='cadastro_academia'),
    path('academia/academia_hub', views.academia_hub, name='academia_hub'),
]