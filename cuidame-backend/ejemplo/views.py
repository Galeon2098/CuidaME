from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response


# Create your views here.
class EjemploView(APIView):
    def get(self, request):
        output = [{'var1':output.var1, 'var2':output.var2} for output in Ejemplo.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = EjmeploSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)