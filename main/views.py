from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from cuidaMe.forms import ClienteRegistrationForm, CuidadorRegistrationForm, ClienteProfileForm, CuidadorProfileForm
from main.models import Cliente, UserPayment
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

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
def product_page(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        price = stripe.Price.list(product=product_id, limit=1)
        checkout_session = stripe.checkout.Session.create(
			payment_method_types = ['card'],
            line_items = [
				{
					'price': price['data'][0].id,
					'quantity': 1,
				},
			],
			mode = 'payment',
			customer_creation = 'always',
			success_url = settings.REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
			cancel_url = settings.REDIRECT_DOMAIN + '/payment_cancelled',
		)
        return redirect(checkout_session.url, code=303)
    return render(request, 'main/product_page.html')


## use Stripe dummy card: 4242 4242 4242 4242
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


