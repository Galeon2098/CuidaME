from django.conf import settings
from django.db import models

from main.offer.models import Offer

class  ChatRequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_chat_requests')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_chat_requests')
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    time_send = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.receiver}'