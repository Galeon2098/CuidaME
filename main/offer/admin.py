from django.contrib import admin
from .models import Offer, Review

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'offer_type', 'client', 'description', 'price_per_hour', 'city', 'available', 'created', 'updated']
    readonly_fields = ['title', 'offer_type', 'client', 'description', 'price_per_hour', 'city', 'available', 'created', 'updated']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('reviews')
        return queryset

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'offer', 'valoration', 'description')
    list_filter = ('user', 'offer', 'valoration')
    list_editable = ('valoration', 'description')
    exclude = ['slug', ]
