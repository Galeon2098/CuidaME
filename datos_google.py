import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('db.sqlite3')

# Crear un cursor
cursor = conn.cursor()

# Verificar si ya existe algún registro con el dominio '127.0.0.1:8000' en la tabla django_site
cursor.execute("SELECT COUNT(*) FROM django_site WHERE domain = ?", ('127.0.0.1:8000',))
result = cursor.fetchone()[0]

# Si no hay ningún registro con el dominio '127.0.0.1:8000', ejecutar el resto del código
if result == 0:
    # Definir una sentencia SQL de inserción con marcadores de posición para django_site
    sql_insert_django_site = '''INSERT INTO django_site (id, name, domain) VALUES (?, ?, ?)'''
    # Datos a insertar en django_site (tupla de valores)
    datos_django_site = (2, '127.0.0.1:8000', '127.0.0.1:8000')
    # Ejecutar la sentencia SQL de inserción en django_site con los datos
    cursor.execute(sql_insert_django_site, datos_django_site)

    # Definir una sentencia SQL de inserción con marcadores de posición para socialaccount_socialapp
    sql_insert_socialapp = '''INSERT INTO socialaccount_socialapp (id, provider, name, client_id, secret, key, provider_id, settings) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
    # Datos a insertar en socialaccount_socialapp (tupla de valores)
    datos_socialapp = (1, 'google', 'CuidaMe', '315281190119-kfel7gapss534099fo612gbbuab2kj9t.apps.googleusercontent.com', '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', '', '', '{}')
    # Ejecutar la sentencia SQL de inserción en socialaccount_socialapp con los datos
    cursor.execute(sql_insert_socialapp, datos_socialapp)

    # Definir una sentencia SQL de inserción con marcadores de posición para socialaccount_socialapp_sites
    sql_insert_socialapp_sites = '''INSERT INTO socialaccount_socialapp_sites (id, socialapp_id, site_id) VALUES (?, ?, ?)'''
    # Datos a insertar en socialaccount_socialapp_sites (tupla de valores)
    datos_socialapp_sites = (1, 1, 2)
    # Ejecutar la sentencia SQL de inserción en socialaccount_socialapp_sites con los datos
    cursor.execute(sql_insert_socialapp_sites, datos_socialapp_sites)

    # Confirmar la transacción
    conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()
