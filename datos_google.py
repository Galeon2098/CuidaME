from django.conf import settings
import psycopg2
import json
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cuidaMe.settings')
CONFIG_FILE_PATH = 'google_key.json'

# Leer el archivo JSON
with open(CONFIG_FILE_PATH, 'r') as config_file:
    config_data = json.load(config_file)

# Configurar la variable de configuración EMAIL_HOST_PASSWORD
CLIENT_ID = config_data.get('CLIENT_ID')
SECRET = config_data.get('SECRET')
# Datos de conexión a la base de datos PostgreSQL (estos valores deberían ser reemplazados por los reales de tu settings.py)
db_name = settings.DATABASES['default']['NAME']
db_user = settings.DATABASES['default']['USER']
db_password = settings.DATABASES['default']['PASSWORD']
db_host = settings.DATABASES['default']['HOST']
db_port = '5432'


# Conectar a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Crear un cursor
cursor = conn.cursor()

# Verificar si ya existe algún registro con el dominio '127.0.0.1:8000' en la tabla django_site
cursor.execute("SELECT COUNT(*) FROM django_site WHERE domain = %s", ('127.0.0.1:8000',))
result = cursor.fetchone()[0]

# Si no hay ningún registro con el dominio '127.0.0.1:8000', ejecutar el resto del código
if result == 0:
    # Definir una sentencia SQL de inserción con marcadores de posición para django_site
    # Sentencia SQL para actualizar el registro en django_site
    sql_update_django_site = '''UPDATE django_site SET name = %s, domain = %s WHERE id = %s'''

    # Nuevos datos para el registro con id 1 en django_site
    nuevo_nombre = '127.0.0.1:8000'
    nuevo_dominio = '127.0.0.1:8000'

    # Ejecutar la sentencia SQL de actualización en django_site con los nuevos datos
    cursor.execute(sql_update_django_site, (nuevo_nombre, nuevo_dominio, 1))

    # Definir una sentencia SQL de inserción con marcadores de posición para socialaccount_socialapp
    sql_insert_socialapp = '''INSERT INTO socialaccount_socialapp (id, provider, name, client_id, secret, key, provider_id, settings) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    # Datos a insertar en socialaccount_socialapp (tupla de valores)


    datos_socialapp = (1, 'google', 'CuidaMe', CLIENT_ID, SECRET, '', '', '{}')
    # Ejecutar la sentencia SQL de inserción en socialaccount_socialapp con los datos
    cursor.execute(sql_insert_socialapp, datos_socialapp)

    # Definir una sentencia SQL de inserción con marcadores de posición para socialaccount_socialapp_sites
    sql_insert_socialapp_sites = '''INSERT INTO socialaccount_socialapp_sites (id, socialapp_id, site_id) VALUES (%s, %s, %s)'''
    # Datos a insertar en socialaccount_socialapp_sites (tupla de valores)
    datos_socialapp_sites = (1, 1, 1)
    # Ejecutar la sentencia SQL de inserción en socialaccount_socialapp_sites con los datos
    cursor.execute(sql_insert_socialapp_sites, datos_socialapp_sites)

    # Confirmar la transacción
    conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()
