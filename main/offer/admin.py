from django.contrib import admin
from .models import Offer

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['title','offer_type','client','description','price_per_hour','city','available','created','updated']
    readonly_fields = ['title','offer_type','client','description','price_per_hour','city','available','created','updated']