from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseForbidden
from .models import Offer, Review
from .forms import OfferForm, ReviewForm
import datetime
from main.models import Cliente, Cuidador
from django.views.decorators.http import require_http_methods
@login_required
def publishOffer(request):
    cuidador = Cuidador.objects.filter(user=request.user).exists()
    if not cuidador:
        return render(request, 'main/error_page.html')
    if Offer.objects.filter(user=request.user).count() >= 5:
      return render(request, 'main/error_page.html')
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
    form = ReviewForm()
    offer_reviews = Review.objects.filter(offer__user = offer.user)
    return render(request, 'offers/detail.html', {'offer': offer, 'form': form, 'offer_reviews': offer_reviews})
#SEARCH  BAR OFFERS
def searchOffers(request):
    search_query = request.POST.get('search_query', '')
    offers = Offer.objects.all()
    if search_query:
        offers = offers.filter(Q(title__icontains=search_query) | Q(city__icontains=search_query) | Q(client__icontains=search_query) | Q(created__icontains=search_query) | Q(price_per_hour__icontains=search_query) |Q(offer_type__icontains=search_query))
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
            return redirect('offer:my_offers')
    else:
        form = OfferForm(instance=offer, user=request.user)  # Pasa el usuario como argumento
    return render(request, 'offers/edit_offer.html', {'form': form, 'offer': offer})
@login_required
def delete_offer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    if request.user != offer.user:
        return HttpResponseForbidden("No tienes permiso para eliminar esta oferta.")
    if request.method == 'POST':
        offer.delete()
        messages.success(request, 'La oferta ha sido eliminada exitosamente.')
        return redirect('offer:my_offers')
    return render(request, 'offers/delete_confirmation.html', {'offer': offer})
@login_required
def myOffers(request):
    offers = Offer.objects.filter(user=request.user)
    show_publish_button = Offer.objects.filter(user_id=request.user).count() < 5
    return render(request, 'offers/myOffers.html', {'offers': offers, 'show_publish_button': show_publish_button})
@login_required
def rate_offer(request, id):
    offer = get_object_or_404(Offer, pk=id)
    if request.user == offer.user:
        messages.error(request, "No puedes valorar tu propia oferta.")
        return redirect('offer:detail', id=id)
    if Review.objects.filter(user=request.user, offer=offer).exists():
        messages.error(request, "Ya has valorado esta oferta.")
        return redirect('offer:detail', id=id)
    if hasattr(request.user, 'cuidador') and request.user.cuidador:
        messages.error(request, "No puedes valorar una oferta si eres cuidador.")
        return redirect('offer:detail', id=id)
    if request.method == 'POST':
        valoration = request.POST.get('rating')
        if valoration is not None:
            valoration = int(valoration)
            description = request.POST.get('commentary')
            review = Review(user=request.user, offer=offer, valoration=valoration, description=description)
            review.save()
            offer.save()
            messages.success(request, "La valoración ha sido guardada exitosamente.")
        else:
            messages.error(request, "Tienes que seleccionar una valoración.")
            return redirect('offer:detail', id=id)
    return redirect('offer:detail', id=id)
def offer_detail(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    form = ReviewForm()
    offer_reviews = Review.objects.filter(offer=offer)
    return render(request, 'offers/detail.html', {'offer': offer, 'form': form, 'offer_reviews': offer_reviews})
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
@user_passes_test(lambda u: u.is_superuser)
@staff_member_required
@require_http_methods(["GET"])
def administrar_ofertas(request):
    ofertas = Offer.objects.all()
    return render(request, 'offers/administrar_ofertas.html', {'ofertas': ofertas})
@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["GET","POST"])
def editar_oferta_admin(request, offer_id):
    oferta = get_object_or_404(Offer, pk=offer_id)
    if request.method == 'POST':
        form = OfferForm(request.POST, instance=oferta)
        if form.is_valid():
            form.save()
            return redirect('offer:administrar_ofertas')
    else:
        form = OfferForm(instance=oferta)  
    return render(request, 'offers/editar_oferta_admin.html', {'form': form, 'oferta': oferta})
@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["GET","POST"])
def eliminar_oferta_admin(request, offer_id):
    oferta = get_object_or_404(Offer, pk=offer_id)  
    if request.method == 'POST':
        oferta.delete()
        return redirect('offer:administrar_ofertas')
    elif request.method == 'GET':
        return render(request, 'offers/eliminar_oferta_admin.html', {'oferta': oferta})