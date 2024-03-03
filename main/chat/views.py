from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import ChatRequest

@login_required
def chat_room(request, chat_id):
    chat_request = get_object_or_404(ChatRequest, id=chat_id)
    if request.user == chat_request.sender or request.user == chat_request.receiver:
        return render(request, 'chat/room.html', {'chat_request': chat_request})
    else:
        return HttpResponseForbidden()
