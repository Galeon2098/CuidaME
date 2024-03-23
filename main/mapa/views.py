import geocoder
from django.shortcuts import render
from django.urls import reverse
import geopy
from main.offer.models import Offer
import folium
from folium.plugins import FastMarkerCluster
from folium import Marker, Popup

def mapaHome(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        geopy.geocoders.options.default_user_agent = "cuidaME"
        g = geocoder.osm(address)
        if g.ok:
            lat, lng = g.latlng
            # Usamos un zoom mayor para las búsquedas
            initialMap = folium.Map(location=[lat, lng], zoom_start=16)
        else:
            initialMap = folium.Map(location=[37.3887735, -5.9835773], zoom_start=13)
    else:
        initialMap = folium.Map(location=[37.3887735, -5.9835773], zoom_start=13)  # Sevilla

    marker_cluster = FastMarkerCluster([], name="Offers")
    marker_cluster.add_to(initialMap)

    offers = Offer.objects.all()

    for offer in offers:
        offer_url = request.build_absolute_uri(reverse('offer:detail', args=[offer.id]))
        type_name = dict(Offer.TYPE_CHOICES)[offer.offer_type]
        popup_html = f'<h3><a href="{offer_url}" target="_blank">{offer.title}</a></h3><strong>Descripción:</strong> {offer.description}<br><strong>Tipo:</strong> {type_name}<br><strong>Precio:</strong> {offer.price_per_hour}'
        popup = Popup(popup_html, max_width=200)
        Marker([offer.lat, offer.lng], popup=popup).add_to(marker_cluster)

    context = {'map': initialMap._repr_html_(), 'offers': offers}
    return render(request, 'mapa/mapa.html', context)
