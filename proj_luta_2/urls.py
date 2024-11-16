from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView  # Importação necessária
from app_luta import views

urlpatterns = [
    # Admin Routes
    path('admin/', admin.site.urls, name='admin'),

    # Home Page
    path('', views.index, name='index'),

    # Organizador Routes
    path('organizador/', views.organizador, name='organizador'),

    # Academia Routes
    path('academia/', views.academia, name='academia'),
    path('academia/cadastro/', views.cadastro_academia, name='cadastro_academia'),

    # Login Routes
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    # Academia Hub (depois de login)
    path('academia/hub/', views.academia_hub, name='academia_hub'),

    path('academia/hub/cadastro_lutador/', views.cadastro_lutador, name='cadastro_lutador'),
]
