from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from cuidaMe.forms import ClienteRegistrationForm, CuidadorRegistrationForm, ClienteProfileForm, CuidadorProfileForm
from main.models import Cliente
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

from main.offer.models import ChatRequest

# Create your views here.
def index(request):
    return render(request, 'main/home.html')

def register_cliente(request):
    if request.method == 'POST':
        user_form = ClienteRegistrationForm(request.POST)
        if user_form.is_valid():
            # Guarda el formulario y sus datos
            user = user_form.save()
            return render(request, 'main/register_done.html', {'new_user': user})
    else:
        user_form = ClienteRegistrationForm()
    return render(request, 'main/register_cliente.html', {'user_form': user_form})

def register_cuidador(request):
    if request.method == 'POST':
        user_form = CuidadorRegistrationForm(request.POST)
        if user_form.is_valid():
            # Guarda el formulario y sus datos
            user = user_form.save()
            return render(request, 'main/register_done.html', {'new_user': user})
    else:
        user_form = CuidadorRegistrationForm()
    return render(request, 'main/register_cuidador.html', {'user_form': user_form})

@login_required
def my_profile_detail(request):
    user = request.user
    return render(request, 'main/my_profile_detail.html', {'user': user})

@login_required
def edit_profile(request):
    try:
        profile = request.user.cliente
        form_class = ClienteProfileForm
    except Cliente.DoesNotExist:
        profile = request.user.cuidador
        form_class = CuidadorProfileForm

    if request.method == 'POST':
        form = form_class(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my_profile_detail')
    else:
        form = form_class(instance=profile)

    return render(request, 'main/edit_profile.html', {'form': form})

@login_required
def profile_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'main/profile_detail.html', {'user': user})

def about_us(request):
    return render(request, 'main/aboutUs.html')

def edit_ad(request):
    return render(request, 'main/edit_ad.html')


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