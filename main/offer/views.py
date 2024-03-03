from django.db.models import Q  
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from main.models import Cliente, Cuidador
from .models import ChatRequest, Offer
from .forms import OfferForm
import datetime

@login_required
def publishOffer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            new_offer = form.save(commit=False)
            new_offer.user = request.user
            new_offer.available = True
            new_offer.created = datetime.datetime.now()
            new_offer.updated = datetime.datetime.now()          
            new_offer.save()
            offers = Offer.objects.filter(user=request.user)
            return redirect('/offer/my_offers')  # Redirige a la vista de mis ofertas
    else:
        form = OfferForm()
    return render(request, 'offers/publish.html', {'form': form})

#LIST OFFERS
def listOffers(request):
    offers = Offer.objects.filter(available=True)
    return render(request, 'offers/list.html', {'offers': offers})
#OFFER DETAIL
def offerDetail(request, id):
    offer = get_object_or_404(Offer, id=id, available=True)
    return render(request, 'offers/detail.html', {'offer': offer})

#SEARCH  BAR OFFERS
def searchOffers(request):
    search_query = request.POST.get('search_query', '')

    offers = Offer.objects.all()

    if search_query:
        offers = offers.filter(Q(city__icontains=search_query) | Q(client__icontains=search_query) | Q(created__icontains=search_query) | Q(price_per_hour__icontains=search_query) |Q(offer_type__icontains=search_query))
    
    return render(request, 'offers/search_results.html', {'offers': offers, 'search_query': search_query})

#FILTER OFFERS
def filterOffers(request):
    min_price_filter = request.POST.get('min_price_filter')
    max_price_filter = request.POST.get('max_price_filter')
    cliente_type_filter = request.POST.get('cliente_type_filter')
    offer_type_filter = request.POST.get('offer_type_filter')
    offers = Offer.objects.all()
    
    if(min_price_filter):
        offers = offers.filter(price_per_hour__gte=min_price_filter)
    if(max_price_filter):
        offers = offers.filter(price_per_hour__lte=max_price_filter)
    if(cliente_type_filter):
        offers = offers.filter(client__icontains=cliente_type_filter)
    if(offer_type_filter):
        offers = offers.filter(offer_type__icontains=offer_type_filter)
    
   
    return render(request, 'offers/list.html', {'offers': offers, 'min_price_filter' : min_price_filter, 'max_price_filter': max_price_filter, 
                                                'cliente_type_filter':cliente_type_filter, 'offer_type_filter':offer_type_filter } )
@login_required
def edit_offer(request, id):
    offer = get_object_or_404(Offer, pk=id)

    if request.user != offer.user:
        return HttpResponseForbidden("No tienes permiso para editar esta oferta.")
    
    if request.method == 'POST':
        form = OfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            offers = Offer.objects.filter(user=request.user)
            return render(request, 'offers/myOffers.html', {'offers': offers})
    else:
        form = OfferForm(instance=offer)
    
    return render(request, 'offers/publish.html', {'form': form, 'offer': offer})


@login_required
def myOffers(request):
    offers = Offer.objects.filter(user=request.user)
    return render(request, 'offers/myOffers.html', {'offers': offers})


@login_required
def send_chat_request(request, cuidador_id, offer_id):
    cliente = get_object_or_404(Cliente, user=request.user)
    cuidador = get_object_or_404(Cuidador, id=cuidador_id)
    oferta = get_object_or_404(Offer, id=offer_id)
    # Verifica si ya existe una solicitud pendiente para esta oferta
    existing_request = ChatRequest.objects.filter(sender=cliente.user, receiver=cuidador.user,accepted=False,offer=oferta).first()
    if not existing_request:
        # Si no existe, crea una nueva solicitud con la oferta asociada
        ChatRequest.objects.create(sender=cliente.user, receiver=cuidador.user, offer=oferta)
    return redirect('offer:list')  

