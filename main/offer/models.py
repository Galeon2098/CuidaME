from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from main.models import Cuidador

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
    POB_CHOICES = [
    ('Alanís', 'Alanís'),
    ('Albaida del Aljarafe', 'Albaida del Aljarafe'),
    ('Alcalá de Guadaíra', 'Alcalá de Guadaíra'),
    ('Alcalá del Río', 'Alcalá del Río'),
    ('Alcolea del Río', 'Alcolea del Río'),
    ('Algámitas', 'Algámitas'),
    ('Almadén de la Plata', 'Almadén de la Plata'),
    ('Almensilla', 'Almensilla'),
    ('Arahal', 'Arahal'),
    ('Aznalcázar', 'Aznalcázar'),
    ('Aznalcóllar', 'Aznalcóllar'),
    ('Badolatosa', 'Badolatosa'),
    ('Benacazón', 'Benacazón'),
    ('Bollullos de la Mitación', 'Bollullos de la Mitación'),
    ('Bormujos', 'Bormujos'),
    ('Brenes', 'Brenes'),
    ('Burguillos', 'Burguillos'),
    ('Camas', 'Camas'),
    ('Cantillana', 'Cantillana'),
    ('Cañada Rosal', 'Cañada Rosal'),
    ('Carmona', 'Carmona'),
    ('Carrión de los Céspedes', 'Carrión de los Céspedes'),
    ('Casariche', 'Casariche'),
    ('Castilblanco de los Arroyos', 'Castilblanco de los Arroyos'),
    ('Castilleja de Guzmán', 'Castilleja de Guzmán'),
    ('Castilleja de la Cuesta', 'Castilleja de la Cuesta'),
    ('Castilleja del Campo', 'Castilleja del Campo'),
    ('Cazalla de la Sierra', 'Cazalla de la Sierra'),
    ('Constantina', 'Constantina'),
    ('Coria del Río', 'Coria del Río'),
    ('Coripe', 'Coripe'),
    ('Dos Hermanas', 'Dos Hermanas'),
    ('Écija', 'Écija'),
    ('El Castillo de las Guardas', 'El Castillo de las Guardas'),
    ('El Coronil', 'El Coronil'),
    ('El Cuervo de Sevilla', 'El Cuervo de Sevilla'),
    ('El Garrobo', 'El Garrobo'),
    ('El Madroño', 'El Madroño'),
    ('El Palmar de Troya', 'El Palmar de Troya'),
    ('El Pedroso', 'El Pedroso'),
    ('El Real de la Jara', 'El Real de la Jara'),
    ('El Ronquillo', 'El Ronquillo'),
    ('El Rubio', 'El Rubio'),
    ('El Saucejo', 'El Saucejo'),
    ('El Viso del Alcor', 'El Viso del Alcor'),
    ('Espartinas', 'Espartinas'),
    ('Estepa', 'Estepa'),
    ('Fuentes de Andalucía', 'Fuentes de Andalucía'),
    ('Gelves', 'Gelves'),
    ('Gerena', 'Gerena'),
    ('Gilena', 'Gilena'),
    ('Gines', 'Gines'),
    ('Guadalcanal', 'Guadalcanal'),
    ('Guillena', 'Guillena'),
    ('Herrera', 'Herrera'),
    ('Huévar del Aljarafe', 'Huévar del Aljarafe'),
    ('Isla Mayor', 'Isla Mayor'),
    ('La Algaba', 'La Algaba'),
    ('La Campana', 'La Campana'),
    ('La Luisiana', 'La Luisiana'),
    ('La Puebla de Cazalla', 'La Puebla de Cazalla'),
    ('La Puebla de los Infantes', 'La Puebla de los Infantes'),
    ('La Puebla del Río', 'La Puebla del Río'),
    ('La Rinconada', 'La Rinconada'),
    ('La Roda de Andalucía', 'La Roda de Andalucía'),
    ('Las Cabezas de San Juan', 'Las Cabezas de San Juan'),
    ('Las Navas de la Concepción', 'Las Navas de la Concepción'),
    ('Lebrija', 'Lebrija'),
    ('Lora de Estepa', 'Lora de Estepa'),
    ('Lora del Río', 'Lora del Río'),
    ('Los Corrales', 'Los Corrales'),
    ('Los Molares', 'Los Molares'),
    ('Los Palacios y Villafranca', 'Los Palacios y Villafranca'),
    ('Los Rosales', 'Los Rosales'),
    ('Madroñera (El)', 'Madroñera (El)'),
    ('Mairena del Alcor', 'Mairena del Alcor'),
    ('Mairena del Aljarafe', 'Mairena del Aljarafe'),
    ('Marchena', 'Marchena'),
    ('Marinaleda', 'Marinaleda'),
    ('Martín de la Jara', 'Martín de la Jara'),
    ('Molares (Los)', 'Molares (Los)'),
    ('Montellano', 'Montellano'),
    ('Morón de la Frontera', 'Morón de la Frontera'),
    ('Navas de la Concepción (Las)', 'Navas de la Concepción (Las)'),
    ('Olivares', 'Olivares'),
    ('Osuna', 'Osuna'),
    ('Palacios y Villafranca (Los)', 'Palacios y Villafranca (Los)'),
    ('Palomares del Río', 'Palomares del Río'),
    ('Paradas', 'Paradas'),
    ('Pedrera', 'Pedrera'),
    ('Pedroso (El)', 'Pedroso (El)'),
    ('Peñaflor', 'Peñaflor'),
    ('Pilas', 'Pilas'),
    ('Pruna', 'Pruna'),
    ('Puebla de Cazalla (La)', 'Puebla de Cazalla (La)'),
    ('Puebla de los Infantes (La)', 'Puebla de los Infantes (La)'),
    ('Puebla del Río (La)', 'Puebla del Río (La)'),
    ('Real de la Jara (El)', 'Real de la Jara (El)'),
    ('Rinconada (La)', 'Rinconada (La)'),
    ('Roda de Andalucía (La)', 'Roda de Andalucía (La)'),
    ('Ronquillo (El)', 'Ronquillo (El)'),
    ('Rubio (El)', 'Rubio (El)'),
    ('Salteras', 'Salteras'),
    ('San Juan de Aznalfarache', 'San Juan de Aznalfarache'),
    ('San Nicolás del Puerto', 'San Nicolás del Puerto'),
    ('Sanlúcar la Mayor', 'Sanlúcar la Mayor'),
    ('Santiponce', 'Santiponce'),
    ('Saucejo (El)', 'Saucejo (El)'),
    ('Sevilla', 'Sevilla'),
    ('Tocina', 'Tocina'),
    ('Tomares', 'Tomares'),
    ('Umbrete', 'Umbrete'),
    ('Utrera', 'Utrera'),
    ('Valencina de la Concepción', 'Valencina de la Concepción'),
    ('Villamanrique de la Condesa', 'Villamanrique de la Condesa'),
    ('Villanueva de San Juan', 'Villanueva de San Juan'),
    ('Villanueva del Ariscal', 'Villanueva del Ariscal'),
    ('Villanueva del Río y Minas', 'Villanueva del Río y Minas'),
    ('Villaverde del Río', 'Villaverde del Río')
]

    title = models.CharField(max_length=75, verbose_name='Título')
    offer_type = models.CharField(max_length=255, verbose_name='Tipo de oferta', choices=TYPE_CHOICES, default='OT')
    client = models.CharField(max_length=255, verbose_name='Tipo de cliente', choices=CLIENT_CHOICES, default='OT')
    description = models.TextField(blank=True)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1.00), MaxValueValidator(100.00)])
    poblacion = models.CharField(max_length=200, verbose_name='Población', choices=POB_CHOICES, default='Sevilla')  
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Cuidador.add_to_class('Total_average_rating', models.FloatField(default=0))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('offer:detail', args=[self.id])

    def calculate_total_average_rating(self):
        user_offers = Offer.objects.filter(user=self.user)
        reviews = Review.objects.filter(offer__in=user_offers)
        valorations = [review.valoration for review in reviews]
        return sum(valorations) / len(valorations) if valorations else 0

    def save(self, *args, **kwargs):
        if hasattr(self.user, 'cuidador') and self.user.cuidador:
            self.user.cuidador.Total_average_rating = self.calculate_total_average_rating()
            self.user.cuidador.save()
        super().save(*args, **kwargs)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='reviews')
    description = models.CharField(max_length=200)
    valoration = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return str(self.user.username)
