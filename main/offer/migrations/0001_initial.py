# Generated by Django 4.1.1 on 2024-03-16 11:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Título')),
                ('offer_type', models.CharField(choices=[('CO', 'COMPAÑÍA'), ('CU', 'CUIDADO'), ('TR', 'TRANSPORTE'), ('DO', 'COMPRA A DOMICILIO'), ('OT', 'OTROS')], default='OT', max_length=255, verbose_name='Tipo de oferta')),
                ('client', models.CharField(choices=[('DF', 'DISCAPACIDAD FÍSICA'), ('DM', 'DISCAPACIDAD MENTAL'), ('NI', 'NIÑOS'), ('AN', 'ANCIANOS'), ('OT', 'OTROS')], default='OT', max_length=255, verbose_name='Tipo de cliente')),
                ('description', models.TextField(blank=True)),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(100.0)])),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('lat', models.FloatField(verbose_name='Latitud')),
                ('lng', models.FloatField(verbose_name='Longitud')),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('valoration', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='offer.offer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
