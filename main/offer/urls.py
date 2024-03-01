from django.urls import path
from .views import filterOffers, listOffers, offerDetail, searchOffers, publishOffer, edit_offer, myOffers, rate_offer

app_name = 'offer'

urlpatterns = [
    path('search/', searchOffers, name='searchOffers'),
    path('filter/', filterOffers, name='filterOffers'),
    path('', publishOffer, name='publish_offer'),
    path('list/', listOffers, name='list'),
    path('list/<int:id>/', offerDetail, name='detail'),
    path('<int:id>/update/', edit_offer, name='update'),

    path('my_offers/', myOffers, name='my_offers'),
    path('<int:id>/review/', rate_offer, name='review'),
]
