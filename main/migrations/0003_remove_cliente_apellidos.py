# Generated by Django 4.1.1 on 2024-03-20 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_cliente_tipo_dependencia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='apellidos',
        ),
    ]
