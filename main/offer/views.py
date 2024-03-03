from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Offer, Review
from .forms import OfferForm, ReviewForm
import datetime
from django.db.models import Avg

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
            return redirect('/offer/my_offers')
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
def rate_offer(request, id):
    offer = get_object_or_404(Offer, pk=id)

    if request.user == offer.user:
        messages.error(request, "No puedes valorar tu propia oferta.")
        return redirect('offer:detail', id=id)

    if Review.objects.filter(user=request.user, offer=offer).exists():
        messages.error(request, "Ya has valorado esta oferta.")
        return redirect('offer:detail', id=id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            valoration = form.cleaned_data['valoration']
            description = form.cleaned_data['description']
            review = Review(user=request.user, offer=offer, valoration=valoration, description=description)
            review.save()

            # Recalcular la media total de la oferta después de valorarla
            offer.average_rating = offer.calculate_average_rating()
            offer.save()

            # Redireccionar a la vista de detalle de la oferta después de valorarla
            return redirect('offer:detail', id=id)
    else:
        form = ReviewForm()
    return render(request, 'offers/rate_offer.html', {'form': form, 'offer': offer})

def offer_detail(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    form = ReviewForm()
    offer_reviews = Review.objects.filter(offer=offer)

    return render(request, 'offers/detail.html', {'offer': offer, 'form': form, 'offer_reviews': offer_reviews})

