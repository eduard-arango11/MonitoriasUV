from django.db import models
from Facultades.models import Facultad

ESTADOS = (('Activo','Activo'),('Inactivo','Inactivo'))

class Unidad(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre de la unidad", unique=True)
    estado = models.CharField(max_length=10, verbose_name="Estado", choices=ESTADOS, default='Activo')
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre