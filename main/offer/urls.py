from django.urls import path
from .views import filterOffers, listOffers, offerDetail,searchOffers, publishOffer,edit_offer, send_chat_request,myOffers


app_name = 'offer'

urlpatterns = [
    path('search/', searchOffers, name='searchOffers'),
    path('filter/', filterOffers, name='filterOffers'),
    path('', publishOffer, name='publish'),
    path('list/', listOffers, name='list'),
    path('list/<int:id>/', offerDetail, name='detail'),
    path('<int:id>/', edit_offer,name='update'),
    path('publish/', publishOffer, name='publish'),
    path('my_offers', myOffers, name='my_offers'),
    path('send_chat_request/<int:cuidador_id>/<int:offer_id>/', send_chat_request, name='send_chat_request'),
]