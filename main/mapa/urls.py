from django.urls import path
from .views import mapaHome

app_name = 'mapa'

urlpatterns = [
    path('', mapaHome, name='mapa'),

]
