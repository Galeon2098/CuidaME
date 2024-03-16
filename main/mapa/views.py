from django.shortcuts import render
from django.urls import reverse
from main.offer.models import Offer
import folium
from folium.plugins import FastMarkerCluster
from folium import Marker, Popup, IFrame

def mapaHome(request):
    offers = Offer.objects.all()

    initialMap = folium.Map(location=[37.3887735,-5.9835773], zoom_start=13) #Sevilla

    latitudes = [offer.lat for offer in offers]
    longitudes = [offer.lng for offer in offers]
    popups = [offer.title for offer in offers]

    for lat, lng, popup, offer in zip(latitudes, longitudes, popups, offers):
        offer_url = request.build_absolute_uri(reverse('offer:detail', args=[offer.id]))
        popup_html = f'<a href="{offer_url}" target="_blank">{popup}</a><br>Title: {offer.title}<br>Description: {offer.description}<br>Type: {offer.offer_type}<br>Price: {offer.price_per_hour}'
        iframe = IFrame(popup_html, width=200, height=100)
        popup = Popup(iframe, max_width=200)
        marker = Marker([lat, lng], popup=popup)
        marker.add_to(initialMap)

    context = {'map':initialMap._repr_html_(), 'offers':offers}
    return render(request, 'mapa/mapa.html', context)