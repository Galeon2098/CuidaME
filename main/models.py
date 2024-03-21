from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    apellidos = models.CharField(max_length=100)

    OPCIONES_DEPENDENCIA = [
        ('personaSolitaria', 'Persona Solitaria'),
        ('enfermedad', 'Enfermedad'),
        ('cuidados', 'Cuidados'),
    ]
    
    tipo_dependencia = models.CharField(max_length=20, choices=OPCIONES_DEPENDENCIA)
    chat_requests_sent = models.ManyToManyField('chat.ChatRequest', related_name='client_sent_requests')
    def __str__(self):
        return self.user.username

class Cuidador(models.Model):

    CLIENT_CHOICES = (
        ('DF', 'DISCAPACIDAD FÍSICA'),
        ('DM', 'DISCAPACIDAD MENTAL'),
        ('NI', 'NIÑOS'),
        ('AN', 'ANCIANOS'),
        ('OT', 'OTROS')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dni = models.CharField(max_length=9, unique=True)
    numero_seguridad_social = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField()
    formacion = models.TextField()
    experiencia = models.TextField()
    tipo_publico_dirigido = models.CharField(max_length=50, choices=CLIENT_CHOICES, default='OT')
    chat_requests_received = models.ManyToManyField('chat.ChatRequest', related_name='caregiver_received_requests', blank=True)
    def __str__(self):
        return self.user.username


class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)
    
