from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Offer
from .forms import OfferForm
import datetime

@login_required
def publishOffer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            new_offer = form.save(commit=False)
            new_offer.user = request.user
            new_offer.available= True
            new_offer.created = datetime.datetime.now()
            new_offer.updated = datetime.datetime.now()          
            new_offer.save()
            offers = Offer.objects.filter(user=request.user)
            return render(request, 'offers/myOffers.html', {'offers': offers})

    else:
        form = OfferForm()
    return render(request,
                'offers/publish.html',
                {'form': form})

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