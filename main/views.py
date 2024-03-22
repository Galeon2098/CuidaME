from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from cuidaMe.forms import ClienteRegistrationForm, CuidadorRegistrationForm, ClienteProfileForm, CuidadorProfileForm,SuperuserProfileForm,InteresForm
from main.models import Cliente, UserPayment
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
import stripe
from django.conf import settings
from django.views.decorators.http import require_http_methods
from .models import Cliente, Cuidador, Interes

# Create your views here.
@require_http_methods(["GET"])
def start_page(request):
    return render(request, 'main/startPage.html')
def index(request):
    return render(request, 'main/home.html')

def pricing_plan(request):
    return render(request, 'main/pricingPlan.html')

def register_cliente(request):
    if request.method == 'POST':
        user_form = ClienteRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            # Guarda el formulario y sus datos
            user = user_form.save()
            return render(request, 'registration/register_done.html', {'new_user': user})
        else:
            # Si el formulario no es válido, mostrar el formulario con los errores
            return render(request, 'registration/register_cliente.html', {'form': user_form})
    else:
        user_form = ClienteRegistrationForm()
    return render(request, 'registration/register_cliente.html', {'user_form': user_form})

def register_cuidador(request):
    if request.method == 'POST':
        user_form = CuidadorRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            # Guarda el formulario y sus datos
            user = user_form.save()
            return render(request, 'registration/register_done.html', {'new_user': user})
        else:
            # Si el formulario no es válido, mostrar el formulario con los errores
            return render(request, 'registration/register_cuidador.html', {'form': user_form})
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
    if request.user.is_superuser:
        profile = request.user
        form_class = SuperuserProfileForm
    else:
        try:
            profile = request.user.cliente
            form_class = ClienteProfileForm
        except Cliente.DoesNotExist:
            profile = request.user.cuidador
            form_class = CuidadorProfileForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=profile)
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

# CRUD INTERESES

# LIST
@login_required
def list_intereses(request):
    cliente = Cliente.objects.filter(user=request.user).exists()
    if not cliente:
        return render(request, 'main/error_page.html')
    intereses = Interes.objects.filter(user=request.user)
    return render(request, 'main/misIntereses.html', {'intereses': intereses})

# CREATE
@login_required
def create_interes(request):
    cliente = Cliente.objects.filter(user=request.user).exists()
    if not cliente:
        return render(request, 'main/error_page.html')
    if request.method == 'POST':
        form = InteresForm(request.POST)
        if form.is_valid():
            new_interes = form.save(commit=False)
            new_interes.user = request.user
            new_interes.save()
            return redirect('mis_intereses')
    else:
        form = InteresForm()
    return render(request, 'main/interesCreate.html', {'form': form})

#UPDATE
@login_required
def edit_interes(request, id):
    interes = get_object_or_404(Interes, pk=id)
    if request.user != interes.user:
        return HttpResponseForbidden("No tienes permiso para editar este interés.")
    if request.method == 'POST':
        form = InteresForm(request.POST, instance=interes)
        if form.is_valid():
            form.save()
            return redirect('mis_intereses')
    else:
        form = InteresForm(instance=interes, user=request.user)
    return render(request, 'main/edit_interes.html', {'form': form, 'interes': interes})

#DELETE
@login_required
def delete_interes(request, interes_id):
    interes = get_object_or_404(Interes, pk=interes_id)
    if request.user != interes.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este interés.")
    if request.method == 'POST':
        interes.delete()
        messages.success(request, 'El interés ha sido eliminado exitosamente.')
        return redirect('mis_intereses')
    return render(request, 'main/delete_interes_confirmation.html', {'interes': interes})


def about_us(request):
    return render(request, 'main/aboutUs.html')

def privacy_policy(request):
    return render(request,'main/privacy_policy.html')

def edit_ad(request):
    return render(request, 'main/edit_ad.html')


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
@require_http_methods(["POST"])
def user_list(request):
    users = User.objects.all()
    return render(request, 'main/user_list.html', {'users': users})


@login_required
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["POST"])
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'main/user_delete.html', {'user': user})

@login_required
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["GET"])
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'main/cliente_list.html', {'clientes': clientes})
@login_required
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["GET"])
def cuidador_list(request):
    cuidadores = Cuidador.objects.all()
    return render(request, 'main/cuidador_list.html', {'cuidadores': cuidadores})
@login_required
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["GET","POST"])
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
@require_http_methods(["GET","POST"])
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
@require_http_methods(["GET","POST"])
def cliente_delete(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'main/cliente_confirm_delete.html', {'cliente': cliente})

@login_required
@user_passes_test(lambda u: u.is_superuser)
@require_http_methods(["GET","POST"])
def cuidador_delete(request, cuidador_id):
    cuidador = get_object_or_404(Cuidador, pk=cuidador_id)
    if request.method == 'POST':
        cuidador.delete()
        return redirect('cuidador_list')
    return render(request, 'main/cuidador_confirm_delete.html', {'cuidador': cuidador})
