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
    User.add_to_class('Total_average_rating', models.FloatField(default=0))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('offer:detail', args=[self.id])

    def calculate_average_rating(self):
        reviews = self.reviews.all()
        valorations = [review.valoration for review in reviews]
        return sum(valorations) / len(valorations) if valorations else 0

    def calculate_total_average_rating(self):
        user_offers = Offer.objects.filter(user=self.user)
        reviews = Review.objects.filter(offer__in=user_offers)
        valorations = [review.valoration for review in reviews]
        return sum(valorations) / len(valorations) if valorations else 0

    def save(self, *args, **kwargs):
        self.user.Total_average_rating = self.calculate_total_average_rating()
        self.user.save()
        super().save(*args, **kwargs)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='reviews')
    description = models.CharField(max_length=200)
    valoration = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return str(self.user.username)
