from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cuidaMe.forms import ClienteRegistrationForm, CuidadorRegistrationForm

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

def about_us(request):
    return render(request, 'main/aboutUs.html')

def edit_ad(request):
    return render(request, 'main/edit_ad.html')

