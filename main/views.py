from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/home.html')

def pricing_plan(request):
    return render(request, 'main/pricingPlan.html')