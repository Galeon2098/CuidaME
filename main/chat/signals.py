from django.db.models.signals import post_save
from django.dispatch import receiver

from main.chat.models import ChatRequest

@receiver(post_save, sender=ChatRequest)
def update_sent_chat_requests(sender, instance, created, **kwargs):
    if created:
        instance.sender.cliente.chat_requests_sent.add(instance)

@receiver(post_save, sender=ChatRequest)
def update_received_chat_requests(sender, instance, created, **kwargs):
    if created:
        instance.receiver.cuidador.chat_requests_received.add(instance)
