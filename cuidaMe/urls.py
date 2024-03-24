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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [path('admin/', admin.site.urls),
    path('', views.start_page, name='start_page'),
    path('home/', views.index, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro_cliente/', views.register_cliente, name='registro_cliente'),
    path('registro_cuidador/', views.register_cuidador, name='registro_cuidador'),
    path('about/', views.about_us, name='about_us'),
    path('mi_perfil/', views.my_profile_detail, name='my_profile_detail'),
    path('mi_perfil/editar/', views.edit_profile, name='edit_profile'),
    path('perfil/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('offer/', include('main.offer.urls', namespace='offer')),
    path('about/', views.about_us, name='about_us'),
    path('edit_ad/', views.edit_ad, name='edit_ad'),
    path('chat/', include('main.chat.urls', namespace='chat')),
    path('pricingPlan/', views.pricing_plan, name='pricing_plan'),
    path('mapa/', include('main.mapa.urls', namespace='mapa')),
    path('privacy_policy',views.privacy_policy, name='privacy_policy'),
    path('product_page/', views.product_page, name='product_page'), # Con fines de testeo
    path('payment_successful/', views.payment_successful, name='payment_successful'),
    path('payment_cancelled/', views.payment_cancelled, name='payment_cancelled'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/<int:cliente_id>/editar/', views.cliente_edit, name='editar_cliente'),
    path('clientes/<int:cliente_id>/delete/', views.cliente_delete, name='eliminar_cliente'),
    path('cuidadores/', views.cuidador_list, name='cuidador_list'),
    path('cuidadores/<int:cuidador_id>/editar/', views.cuidador_edit, name='editar_cuidador'),
    path('cuidadores/<int:cuidador_id>/delete/', views.cuidador_delete, name='eliminar_cuidador'),
    path('foro/', include('main.foro.urls', namespace='foro')),
    path('mis_intereses/', views.list_intereses, name='mis_intereses'),
    path('interes/create/', views.create_interes, name='mis_intereses_create'),
    path('delete_interes/<int:interes_id>/delete/', views.delete_interes, name="delete_interes"),
    path('interes/<int:interes_id>/', views.edit_interes, name="edit_interes"),
]

# Agrega la ruta de medios para servir archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
