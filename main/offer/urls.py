from django.urls import path
from . import views

app_name = 'offer'

urlpatterns = [
    path('', views.publishOffer, name='publish'),
    path('<int:id>/', views.edit_offer,name='update'),
]