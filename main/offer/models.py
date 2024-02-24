from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Offer(models.Model):

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


    title = models.CharField(max_length=200, verbose_name='Título')
    offer_type= models.CharField(max_length=255, verbose_name='Tipo de oferta', choices=TYPE_CHOICES, default='OT')
    client = models.CharField(max_length=255, verbose_name='Tipo de cliente', choices=CLIENT_CHOICES, default='OT')
    description = models.TextField(blank=True)
    price_per_hour = models.DecimalField(max_digits=10,decimal_places=2)
    city = models.CharField(max_length=200, verbose_name='Ciudad')                            
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=200, verbose_name='username',default='cuidador')
    
    def __str__(self):
        return self.title