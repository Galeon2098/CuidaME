from django.contrib import admin
from .models import ChatRequest

@admin.register(ChatRequest)
class ChatRequestAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'timeSend', 'accepted']
    list_filter = ['accepted']
