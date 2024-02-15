from rest_framework import serializers
from .models import *

class EjmeploSerializer(serializers.Serializer):
    class Meta:
        model = Ejemplo
        fields = ['var1', 'var2']