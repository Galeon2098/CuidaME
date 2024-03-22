from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from main.offer.choices import POB_CHOICES

class Cliente(models.Model):
    imagen_perfil = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chat_requests_sent = models.ManyToManyField('chat.ChatRequest', related_name='client_sent_requests')
    def __str__(self):
        return self.user.username

class Cuidador(models.Model):
    imagen_perfil = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    dni_regex = '^[0-9]{8}[A-Za-z]$'  # Expresión regular para validar DNI español
    nss_regex = '^[0-9]{12}$'  # Expresión regular para validar número de seguridad social
    
    dni_validator = RegexValidator(
        regex=dni_regex,
        message='Introduce un DNI válido (8 dígitos seguidos de una letra)'
    )
    
    nss_validator = RegexValidator(
        regex=nss_regex,
        message='Introduce un número de seguridad social válido (12 dígitos)'
    )

    dni = models.CharField(max_length=20, unique=True, validators=[dni_validator])
    numero_seguridad_social = models.CharField(max_length=20, unique=True, validators=[nss_validator])
    descripcion = models.TextField()

    CLIENT_CHOICES = (
        ('DF', 'DISCAPACIDAD FÍSICA'),
        ('DM', 'DISCAPACIDAD MENTAL'),
        ('NI', 'NIÑOS'),
        ('AN', 'ANCIANOS'),
        ('OT', 'OTROS')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    formacion = models.TextField()
    experiencia = models.TextField()
    chat_requests_received = models.ManyToManyField('chat.ChatRequest', related_name='caregiver_received_requests')
    def __str__(self):
        return self.user.username


class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)

class Interes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('CO', 'COMPAÑÍA'),
        ('CU', 'CUIDADO'),
        ('TR', 'TRANSPORTE'),
        ('DO', 'COMPRA A DOMICILIO'),
        ('OT', 'OTROS')
    )

    CLIENT_CHOICES = (
        ('DF', 'DISCAPACIDAD FÍSICA'),
        ('DM', 'DISCAPACIDAD MENTAL'),
        ('NI', 'NIÑOS'),
        ('AN', 'ANCIANOS'),
        ('OT', 'OTROS')
    )

    offer_type= models.CharField(max_length=255, verbose_name='Tipo de oferta', choices=TYPE_CHOICES, default='OT')
    client = models.CharField(max_length=255, verbose_name='Tipo de cliente', choices=CLIENT_CHOICES, default='OT')
    poblacion = models.CharField(max_length=200, verbose_name='Población', choices=POB_CHOICES, default='Sevilla')
    
