"""cuidaMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro_cliente/', views.register_cliente, name='registro_cliente'),
    path('registro_cuidador/', views.register_cuidador, name='registro_cuidador'),
    path('mi_perfil/', views.my_profile_detail, name='my_profile_detail'),
    path('mi_perfil/editar', views.edit_profile, name='edit_profile'),
    path('perfil/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('offer/', include('main.offer.urls', namespace='offer'))
]