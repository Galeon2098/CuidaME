from django.contrib import admin
from main.models import Cliente, Cuidador

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['user', 'apellidos', 'tipo_dependencia']
    raw_id_fields = ['user']

@admin.register(Cuidador)
class CuidadorAdmin(admin.ModelAdmin):
    list_display = ['user', 'dni', 'numero_seguridad_social', 'fecha_nacimiento', 'formacion', 'descripcion', 'tipo_publico_dirigido']
    raw_id_fields = ['user']