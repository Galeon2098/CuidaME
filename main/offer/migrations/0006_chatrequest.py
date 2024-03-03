# Generated by Django 4.2.7 on 2024-03-02 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offer', '0005_alter_offer_price_per_hour'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('timeSend', models.DateTimeField(auto_now_add=True)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.offer')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                               related_name='received_chat_requests', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_chat_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
