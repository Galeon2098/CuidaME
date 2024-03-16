from django.shortcuts import render
from main.offer.models import Offer
import folium
from folium.plugins import FastMarkerCluster

def mapaHome(request):
    offers = Offer.objects.all()

    initialMap = folium.Map(location=[37.3887735,-5.9835773], zoom_start=13) #Sevilla

    latitudes = [offer.lat for offer in offers]
    longitudes = [offer.lng for offer in offers]
    popups = [offer.title for offer in offers]

    FastMarkerCluster(data=list(zip(latitudes, longitudes, popups))).add_to(initialMap)

    context = {'map':initialMap._repr_html_(), 'offers':offers}
    return render(request, 'mapa/mapa.html', context)
