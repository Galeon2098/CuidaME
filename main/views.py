from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from cuidaMe.forms import ClienteRegistrationForm, CuidadorRegistrationForm, ClienteProfileForm, CuidadorProfileForm
from main.models import Cliente, UserPayment
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
import stripe
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Cliente, Cuidador
from cuidaMe.forms import ClienteProfileForm, CuidadorProfileForm


from main.offer.models import ChatRequest

def index(request):
    return render(request, 'main/home.html')

def pricing_plan(request):
    return render(request, 'main/pricingPlan.html')

def register_cliente(request):
    if request.method == 'POST':
        user_form = ClienteRegistrationForm(request.POST)
        if user_form.is_valid():
            # Guarda el formulario y sus datos
            user = user_form.save()
            return render(request, 'registration/register_done.html', {'new_user': user})
    else:
        user_form = ClienteRegistrationForm()
    return render(request, 'registration/register_cliente.html', {'user_form': user_form})

def register_cuidador(request):
    if request.method == 'POST':
        user_form = CuidadorRegistrationForm(request.POST)
        if user_form.is_valid():
            # Guarda el formulario y sus datos
            user = user_form.save()
            return render(request, 'registration/register_done.html', {'new_user': user})
    else:
        user_form = CuidadorRegistrationForm()
    return render(request, 'registration/register_cuidador.html', {'user_form': user_form})

def about_us(request):
    return render(request, 'main/aboutUs.html')

@login_required
def edit_ad(request):
    return render(request, 'main/edit_ad.html')

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

    if profile.user != request.user:
        return render(request, 'main/error_page.html')

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


@login_required
@require_http_methods(["GET", "POST"])
def product_page(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        price = stripe.Price.list(product=product_id, limit=1)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price['data'][0].id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            customer_creation='always',
            success_url=settings.REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.REDIRECT_DOMAIN + '/payment_cancelled',
        )

        return redirect(checkout_session.url, code=303)
    return render(request, 'main/product_page.html')


## use Stripe dummy card: 4242 4242 4242 4242
@require_http_methods(["GET"])
def payment_successful(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    checkout_session_id = request.GET.get('session_id', None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)
    user_id = request.user.id
    user_payment = UserPayment.objects.create(
        user_id=user_id,
        payment_bool=True,
        stripe_checkout_id=checkout_session_id
    )
    user_payment.save()
    return render(request, 'main/payment_successful.html', {'customer': customer})


@require_http_methods(["GET"])
def payment_cancelled(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    user_id = request.user.id
    user_payment = UserPayment.objects.create(
        user_id=user_id,
        payment_bool=False,
        stripe_checkout_id=''
    )
    user_payment.save()
    return render(request, 'main/payment_cancelled.html')

# Vistas para el backend (requieren autenticación de superusuario)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    users = User.objects.all()
    return render(request, 'main/user_list.html', {'users': users})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'main/user_delete.html', {'user': user})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'main/cliente_list.html', {'clientes': clientes})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cuidador_list(request):
    cuidadores = Cuidador.objects.all()
    return render(request, 'main/cuidador_list.html', {'cuidadores': cuidadores})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cliente_detail(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteProfileForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('main/cliente_list')
    else:
        form = ClienteProfileForm(instance=cliente)
    return render(request, 'main/cliente_detail.html', {'cliente': cliente, 'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cuidador_detail(request, cuidador_id):
    cuidador = get_object_or_404(Cuidador, pk=cuidador_id)
    if request.method == 'POST':
        form = CuidadorProfileForm(request.POST, instance=cuidador)
        if form.is_valid():
            form.save()
            return redirect('cuidador_list')
    else:
        form = CuidadorProfileForm(instance=cuidador)
    return render(request, 'main/cuidador_detail.html', {'cuidador': cuidador, 'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cliente_edit(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteProfileForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteProfileForm(instance=cliente)
    return render(request, 'main/cliente_edit.html', {'cliente': cliente, 'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cuidador_edit(request, cuidador_id):
    cuidador = get_object_or_404(Cuidador, pk=cuidador_id)
    if request.method == 'POST':
        form = CuidadorProfileForm(request.POST, instance=cuidador)
        if form.is_valid():
            form.save()
            return redirect('cuidador_list')
    else:
        form = CuidadorProfileForm(instance=cuidador)
    return render(request, 'main/cuidador_edit.html', {'cuidador': cuidador, 'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cliente_delete(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'main/cliente_confirm_delete.html', {'cliente': cliente})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cuidador_delete(request, cuidador_id):
    cuidador = get_object_or_404(Cuidador, pk=cuidador_id)
    if request.method == 'POST':
        cuidador.delete()
        return redirect('cuidador_list')
    return render(request, 'main/cuidador_confirm_delete.html', {'cuidador': cuidador})
