from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/home.html')

def about_us(request):
    return render(request, 'main/aboutUs.html')

def edit_ad(request):
    return render(request, 'main/edit_ad.html')

def my_profile_detail(request):
    return render(request, 'main/my_profile_detail.html')

def edit_profile(request):
    return render(request, 'main/edit_profile.html')

def profile_detail(request):
    return render(request, 'main/profile_detail.html')
