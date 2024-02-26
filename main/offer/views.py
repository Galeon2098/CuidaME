from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
            new_offer.available = True
            new_offer.created = datetime.datetime.now()
            new_offer.updated = datetime.datetime.now()          
            new_offer.save()
            offers = Offer.objects.filter(user=request.user)
            return redirect('/offer/my_offers')  # Redirige a la vista de mis ofertas
    else:
        form = OfferForm()
    return render(request, 'offers/publish.html', {'form': form})

@login_required
def myOffers(request):
    offers = Offer.objects.filter(user=request.user)
    return render(request, 'offers/myOffers.html', {'offers': offers})