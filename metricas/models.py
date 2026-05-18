from django.db import models

# Create your models here.
from django.db import models

class metrica_errores(models.Model):
    nombre_error = models.CharField(max_length=200)
    fecha_error = models.DateTimeField("date published")
    cantidad_errores = models.IntegerField(default=0)


class metrica_resultados(models.Model):
    fecha_resultados = models.CharField(max_length=200)
    estadísticas = models.IntegerField(default=0)
    
class metrica_front(models.Model):
    titulos = models.CharField(max_length=200)
    parrafos = models.CharField(max_length=200)
    botones = models.IntegerField(default=0)