from django.db import models

# Create your models here.
class Ejemplo(models.Model):
    var1 = models.CharField(max_length=30)
    var2 = models.CharField(max_length=30)