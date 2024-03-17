from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



class Cliente(models.Model):
    imagen_perfil = models.ImageField(upload_to="imagenes", null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    apellidos = models.CharField(max_length=100)

    OPCIONES_DEPENDENCIA = [
        ('personaSolitaria', 'Persona Solitaria'),
        ('enfermedad', 'Enfermedad'),
        ('cuidados', 'Cuidados'),
    ]
    
    tipo_dependencia = models.CharField(max_length=20, choices=OPCIONES_DEPENDENCIA)
    chat_requests_sent = models.ManyToManyField('offer.ChatRequest', related_name='client_sent_requests')
    def __str__(self):
        return self.user.username

class Cuidador(models.Model):
    imagen_perfil = models.ImageField(upload_to="imagenes", null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    fecha_nacimiento = models.DateField()
    formacion = models.TextField()
    descripcion = models.TextField()

    PUBLICO_DIRIGIDO = [
        ('personaSolitaria', 'Persona Solitaria'),
        ('enfermedad', 'Enfermedad'),
        ('cuidados', 'Cuidados'),
    ]
    tipo_publico_dirigido = models.CharField(max_length=100, choices=PUBLICO_DIRIGIDO)
    chat_requests_received = models.ManyToManyField('offer.ChatRequest', related_name='caregiver_received_requests')
    def __str__(self):
        return self.user.username


class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)
    
