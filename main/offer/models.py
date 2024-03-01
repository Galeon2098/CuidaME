from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    average_rating = models.FloatField(default=0)
    Total_average_rating = models.FloatField(default=0)  

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('offer:detail', args=[self.id])

    def calculate_total_average_rating(self):
        # Obtener todas las ofertas del usuario
        user_offers = Offer.objects.filter(user=self.user)
        # Calcular la suma total de los average_rating de todas las ofertas
        total_rating = sum(offer.average_rating for offer in user_offers)
        # Calcular el promedio de los average_rating
        count = user_offers.count()
        return total_rating / count if count > 0 else 0

    def save(self, *args, **kwargs):
        # Calcular y guardar la media total de la oferta
        self.Total_average_rating = self.calculate_total_average_rating()
        super().save(*args, **kwargs)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    valoration = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return str(self.user.username)
