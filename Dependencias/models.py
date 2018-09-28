from django.db import models

ESTADOS = (('Activo','Activo'),('Inactivo','Inactivo'))

class Dependencia(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre de la dependencia", unique=True)
    estado = models.CharField(max_length=10, verbose_name="Estado", choices=ESTADOS, default='Activo')
    
    def __str__(self):
        return self.nombre