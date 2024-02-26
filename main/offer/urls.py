from django.urls import path
from .views import publishOffer, myOffers

app_name = 'offer'

urlpatterns = [
    path('', publishOffer, name='publish'),
    path('publish/', publishOffer, name='publish'),
    path('my_offers', myOffers, name='my_offers'),
]