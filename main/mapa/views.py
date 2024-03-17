from django.shortcuts import render
from django.urls import reverse
from main.offer.models import Offer
import folium
from folium.plugins import FastMarkerCluster
from folium import Marker, Popup, IFrame

def mapaHome(request):
    offers = Offer.objects.all()

    initialMap = folium.Map(location=[37.3887735, -5.9835773], zoom_start=13)  # Sevilla

    marker_cluster = FastMarkerCluster([], name="Offers")
    marker_cluster.add_to(initialMap)

    for offer in offers:
        offer_url = request.build_absolute_uri(reverse('offer:detail', args=[offer.id]))
        type_name = dict(Offer.TYPE_CHOICES)[offer.offer_type]
        popup_html = f'<h3><a href="{offer_url}" target="_blank">{offer.title}</a></h3><strong>Descripción:</strong> {offer.description}<br><strong>Tipo:</strong> {type_name}<br><strong>Precio:</strong> {offer.price_per_hour}'
        iframe = IFrame(popup_html, width=200, height=120)
        popup = Popup(iframe, max_width=200)
        Marker([offer.lat, offer.lng], popup=popup).add_to(marker_cluster)

    context = {'map': initialMap._repr_html_(), 'offers': offers}
    return render(request, 'mapa/mapa.html', context)
