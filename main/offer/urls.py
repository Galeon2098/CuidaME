from django.urls import path
from .views import filterOffers, listOffers, offerDetail,searchOffers, publishOffer

app_name = 'offer'

urlpatterns = [
    path('search/', searchOffers, name='searchOffers'),
    path('filter/', filterOffers, name='filterOffers'),
    path('', publishOffer, name='publish'),
    path('list/', listOffers, name='list'),
    path('list/<int:id>/', offerDetail, name='detail'),
   
]