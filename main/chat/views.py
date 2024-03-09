from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from main.chat.models import ChatRequest
from main.models import Cliente, Cuidador
from main.offer.models import Offer

@login_required
def chat_room(request, chat_id):
    chat_request = get_object_or_404(ChatRequest, id=chat_id)
    if chat_request.accepted:
        if request.user == chat_request.sender or request.user == chat_request.receiver:
            return render(request, 'chat/room.html', {'chat_request': chat_request})
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseForbidden()

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

@login_required
def chat_requests_for_caregiver(request):
    chat_requests = ChatRequest.objects.filter(receiver=request.user, accepted=False)
    return render(request, 'chat/chat_list.html', {'chat_requests': chat_requests})

#Cuando se acepta te redirige al chat
def accept_chat_request(request, chat_request_id):
    chat_request = get_object_or_404(ChatRequest, id=chat_request_id)
    chat_request.accepted = True
    chat_request.save()
    return redirect(reverse('chat:chat_room', kwargs={'chat_id': chat_request.id}))

def reject_chat_request(request, chat_request_id):
    chat_request = get_object_or_404(ChatRequest, id=chat_request_id)
    chat_request.delete()
    return redirect('chat_requests_for_caregiver')