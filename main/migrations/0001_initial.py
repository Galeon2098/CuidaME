# Generated by Django 4.1.1 on 2024-03-04 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuidador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('numero_seguridad_social', models.CharField(max_length=20, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('formacion', models.TextField()),
                ('experiencia', models.TextField()),
                ('tipo_publico_dirigido', models.CharField(max_length=100)),
                ('chat_requests_received', models.ManyToManyField(related_name='caregiver_received_requests', to='offer.chatrequest')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos', models.CharField(max_length=100)),
                ('tipo_dependencia', models.CharField(choices=[('personaSolitaria', 'Persona Solitaria'), ('enfermedad', 'Enfermedad'), ('cuidados', 'Cuidados')], max_length=20)),
                ('chat_requests_sent', models.ManyToManyField(related_name='client_sent_requests', to='offer.chatrequest')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
