# Generated by Django 4.1.1 on 2024-03-22 21:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_chatmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_bool', models.BooleanField(default=False)),
                ('stripe_checkout_id', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_type', models.CharField(choices=[('CO', 'COMPAÑÍA'), ('CU', 'CUIDADO'), ('TR', 'TRANSPORTE'), ('DO', 'COMPRA A DOMICILIO'), ('OT', 'OTROS')], default='OT', max_length=255, verbose_name='Tipo de oferta')),
                ('client', models.CharField(choices=[('DF', 'DISCAPACIDAD FÍSICA'), ('DM', 'DISCAPACIDAD MENTAL'), ('NI', 'NIÑOS'), ('AN', 'ANCIANOS'), ('OT', 'OTROS')], default='OT', max_length=255, verbose_name='Tipo de cliente')),
                ('poblacion', models.CharField(choices=[('Alanís', 'Alanís'), ('Albaida del Aljarafe', 'Albaida del Aljarafe'), ('Alcalá de Guadaíra', 'Alcalá de Guadaíra'), ('Alcalá del Río', 'Alcalá del Río'), ('Alcolea del Río', 'Alcolea del Río'), ('Algámitas', 'Algámitas'), ('Almadén de la Plata', 'Almadén de la Plata'), ('Almensilla', 'Almensilla'), ('Arahal', 'Arahal'), ('Aznalcázar', 'Aznalcázar'), ('Aznalcóllar', 'Aznalcóllar'), ('Badolatosa', 'Badolatosa'), ('Benacazón', 'Benacazón'), ('Bollullos de la Mitación', 'Bollullos de la Mitación'), ('Bormujos', 'Bormujos'), ('Brenes', 'Brenes'), ('Burguillos', 'Burguillos'), ('Camas', 'Camas'), ('Cantillana', 'Cantillana'), ('Cañada Rosal', 'Cañada Rosal'), ('Carmona', 'Carmona'), ('Carrión de los Céspedes', 'Carrión de los Céspedes'), ('Casariche', 'Casariche'), ('Castilblanco de los Arroyos', 'Castilblanco de los Arroyos'), ('Castilleja de Guzmán', 'Castilleja de Guzmán'), ('Castilleja de la Cuesta', 'Castilleja de la Cuesta'), ('Castilleja del Campo', 'Castilleja del Campo'), ('Cazalla de la Sierra', 'Cazalla de la Sierra'), ('Constantina', 'Constantina'), ('Coria del Río', 'Coria del Río'), ('Coripe', 'Coripe'), ('Dos Hermanas', 'Dos Hermanas'), ('Écija', 'Écija'), ('El Castillo de las Guardas', 'El Castillo de las Guardas'), ('El Coronil', 'El Coronil'), ('El Cuervo de Sevilla', 'El Cuervo de Sevilla'), ('El Garrobo', 'El Garrobo'), ('El Madroño', 'El Madroño'), ('El Palmar de Troya', 'El Palmar de Troya'), ('El Pedroso', 'El Pedroso'), ('El Real de la Jara', 'El Real de la Jara'), ('El Ronquillo', 'El Ronquillo'), ('El Rubio', 'El Rubio'), ('El Saucejo', 'El Saucejo'), ('El Viso del Alcor', 'El Viso del Alcor'), ('Espartinas', 'Espartinas'), ('Estepa', 'Estepa'), ('Fuentes de Andalucía', 'Fuentes de Andalucía'), ('Gelves', 'Gelves'), ('Gerena', 'Gerena'), ('Gilena', 'Gilena'), ('Gines', 'Gines'), ('Guadalcanal', 'Guadalcanal'), ('Guillena', 'Guillena'), ('Herrera', 'Herrera'), ('Huévar del Aljarafe', 'Huévar del Aljarafe'), ('Isla Mayor', 'Isla Mayor'), ('La Algaba', 'La Algaba'), ('La Campana', 'La Campana'), ('La Luisiana', 'La Luisiana'), ('La Puebla de Cazalla', 'La Puebla de Cazalla'), ('La Puebla de los Infantes', 'La Puebla de los Infantes'), ('La Puebla del Río', 'La Puebla del Río'), ('La Rinconada', 'La Rinconada'), ('La Roda de Andalucía', 'La Roda de Andalucía'), ('Las Cabezas de San Juan', 'Las Cabezas de San Juan'), ('Las Navas de la Concepción', 'Las Navas de la Concepción'), ('Lebrija', 'Lebrija'), ('Lora de Estepa', 'Lora de Estepa'), ('Lora del Río', 'Lora del Río'), ('Los Corrales', 'Los Corrales'), ('Los Molares', 'Los Molares'), ('Los Palacios y Villafranca', 'Los Palacios y Villafranca'), ('Los Rosales', 'Los Rosales'), ('Madroñera (El)', 'Madroñera (El)'), ('Mairena del Alcor', 'Mairena del Alcor'), ('Mairena del Aljarafe', 'Mairena del Aljarafe'), ('Marchena', 'Marchena'), ('Marinaleda', 'Marinaleda'), ('Martín de la Jara', 'Martín de la Jara'), ('Molares (Los)', 'Molares (Los)'), ('Montellano', 'Montellano'), ('Morón de la Frontera', 'Morón de la Frontera'), ('Navas de la Concepción (Las)', 'Navas de la Concepción (Las)'), ('Olivares', 'Olivares'), ('Osuna', 'Osuna'), ('Palacios y Villafranca (Los)', 'Palacios y Villafranca (Los)'), ('Palomares del Río', 'Palomares del Río'), ('Paradas', 'Paradas'), ('Pedrera', 'Pedrera'), ('Pedroso (El)', 'Pedroso (El)'), ('Peñaflor', 'Peñaflor'), ('Pilas', 'Pilas'), ('Pruna', 'Pruna'), ('Puebla de Cazalla (La)', 'Puebla de Cazalla (La)'), ('Puebla de los Infantes (La)', 'Puebla de los Infantes (La)'), ('Puebla del Río (La)', 'Puebla del Río (La)'), ('Real de la Jara (El)', 'Real de la Jara (El)'), ('Rinconada (La)', 'Rinconada (La)'), ('Roda de Andalucía (La)', 'Roda de Andalucía (La)'), ('Ronquillo (El)', 'Ronquillo (El)'), ('Rubio (El)', 'Rubio (El)'), ('Salteras', 'Salteras'), ('San Juan de Aznalfarache', 'San Juan de Aznalfarache'), ('San Nicolás del Puerto', 'San Nicolás del Puerto'), ('Sanlúcar la Mayor', 'Sanlúcar la Mayor'), ('Santiponce', 'Santiponce'), ('Saucejo (El)', 'Saucejo (El)'), ('Sevilla', 'Sevilla'), ('Tocina', 'Tocina'), ('Tomares', 'Tomares'), ('Umbrete', 'Umbrete'), ('Utrera', 'Utrera'), ('Valencina de la Concepción', 'Valencina de la Concepción'), ('Villamanrique de la Condesa', 'Villamanrique de la Condesa'), ('Villanueva de San Juan', 'Villanueva de San Juan'), ('Villanueva del Ariscal', 'Villanueva del Ariscal'), ('Villanueva del Río y Minas', 'Villanueva del Río y Minas'), ('Villaverde del Río', 'Villaverde del Río')], default='Sevilla', max_length=200, verbose_name='Población')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cuidador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_perfil', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('dni', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Introduce un DNI válido (8 dígitos seguidos de una letra)', regex='^[0-9]{8}[A-Za-z]$')])),
                ('numero_seguridad_social', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Introduce un número de seguridad social válido (12 dígitos)', regex='^[0-9]{12}$')])),
                ('fecha_nacimiento', models.DateField()),
                ('formacion', models.TextField()),
                ('experiencia', models.TextField()),
                ('Total_average_rating', models.FloatField(default=0)),
                ('chat_requests_received', models.ManyToManyField(related_name='caregiver_received_requests', to='chat.chatrequest')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_perfil', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('chat_requests_sent', models.ManyToManyField(related_name='client_sent_requests', to='chat.chatrequest')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
