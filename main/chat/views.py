import json
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from main.chat.models import ChatMessage, ChatRequest
from main.models import Cliente, Cuidador
from main.offer.models import Offer
from django.contrib.auth.decorators import user_passes_test

@login_required
def chat_room(request, chat_id):
    chat_request = get_object_or_404(ChatRequest, id=chat_id)
    messages = ChatMessage.objects.filter(chat_request=chat_request)
    if chat_request.accepted:
        if request.user == chat_request.sender or request.user == chat_request.receiver:
            return render(request, 'chat/room.html', {'chat_request': chat_request, 'messages': messages})
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
    existing_request = ChatRequest.objects.filter(sender=cliente.user, receiver=cuidador.user, offer=oferta).first()
    if not existing_request:
        # Si no existe, crea una nueva solicitud con la oferta asociada
        ChatRequest.objects.create(sender=cliente.user, receiver=cuidador.user, offer=oferta)
    return redirect('offer:list')

@user_passes_test(lambda user: hasattr(user, 'cuidador'))
def chat_requests_for_caregiver(request):
    chat_requests = ChatRequest.objects.filter(receiver=request.user, accepted=False)
    return render(request, 'chat/chat_list.html', {'chat_requests': chat_requests})

def accept_chat_request(request, chat_request_id):
    chat_request = get_object_or_404(ChatRequest, id=chat_request_id)
    chat_request.accepted = True
    chat_request.save()
    return redirect(reverse('chat:chat_room', kwargs={'chat_id': chat_request.id}))

def reject_chat_request(request, chat_request_id):
    chat_request = get_object_or_404(ChatRequest, id=chat_request_id)
    chat_request.delete()
    referer = request.META.get('HTTP_REFERER')
    if referer and '/chat/chat_rooms' in referer:
        return HttpResponseRedirect(reverse('chat:chat_rooms'))
    else:
        return HttpResponseRedirect(reverse('chat:chat_requests_for_caregiver'))

@login_required
def chat_rooms(request):
    user = request.user
    if user.is_authenticated:
        if hasattr(user, 'cuidador'):
            chat_requests = user.cuidador.chat_requests_received.filter(accepted=True)
        elif hasattr(user, 'cliente'):
            chat_requests = user.cliente.chat_requests_sent.filter(accepted=True)
        else:
            chat_requests = None
        return render(request, 'chat/chat_rooms.html', {'chat_requests': chat_requests})
    else:
        return render(request, 'chat/chat_rooms.html', {})


def send_message(request, chat_request_id):
    chat_request = get_object_or_404(ChatRequest, id=chat_request_id)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            content = data.get('message')

            if content:
                message = ChatMessage.objects.create(user=request.user, chat_request=chat_request, message=content)
                return HttpResponse('Message sent successfully')
            else:
                return HttpResponseBadRequest('Message cannot be empty')
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON format')
    else:
        return HttpResponseNotAllowed(['POST'])