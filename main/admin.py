from django.contrib import admin
from main.models import Cliente, Cuidador
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['user']
    raw_id_fields = ['user']

@admin.register(Cuidador)
class CuidadorAdmin(admin.ModelAdmin):
    list_display = ['user', 'dni', 'numero_seguridad_social', 'fecha_nacimiento', 'formacion', 'experiencia']
    raw_id_fields = ['user']

class CustomUserAdmin(BaseUserAdmin):
    def has_add_permission(self, request):
        return False
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
