from django.urls import path
from .views import publishOffer

app_name = 'offer'

urlpatterns = [
    path('', publishOffer, name='publish'),
]