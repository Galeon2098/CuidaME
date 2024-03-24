from django.urls import path
from .views import filterOffers, listOffers, offerDetail, rate_offer,searchOffers, publishOffer, edit_offer, myOffers, delete_offer,administrar_ofertas,editar_oferta_admin,eliminar_oferta_admin

app_name = 'offer'

urlpatterns = [
    path('search/', searchOffers, name='searchOffers'),
    path('filter/', filterOffers, name='filterOffers'),
    path('', myOffers , name='my_offers'),
    path('list/', listOffers, name='list'),
    path('list/<int:id>/', offerDetail, name='detail'),
    path('<int:id>/update/', edit_offer, name='update'),
    path('my_offers/', myOffers, name='my_offers'),
    path('<int:id>/review/', rate_offer, name='review'),
    path('<int:id>/', edit_offer,name='update'),
    path('publish/', publishOffer, name='publish'),
    path('offer/<int:offer_id>/delete/', delete_offer, name='delete_offer'),
    path('edit_offer/<int:id>', edit_offer, name='edit_offer'),
    path('administrar_ofertas/', administrar_ofertas, name='administrar_ofertas'),
    path('editar_oferta_admin/<int:offer_id>/', editar_oferta_admin, name='editar_oferta_admin'),
    path('eliminar_oferta_admin/<int:offer_id>/', eliminar_oferta_admin, name='eliminar_oferta_admin'),
]
