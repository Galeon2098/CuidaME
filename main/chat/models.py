from django.db import models
from django.conf import settings
from main.offer.models import Offer

class ChatRequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_chat_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_chat_requests', on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    timeSend = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender} to {self.receiver}"
