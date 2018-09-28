from django.db import models
from Facultades.models import Facultad

ESTADOS = (('Activo','Activo'),('Inactivo','Inactivo'))
JORNADAS = (('Diurna','Diurna'),('Nocturna','Nocturna'),('Vespertina','Vespertina'))

class ProgramaAcademico(models.Model):
	nombre_programa = models.CharField(max_length=200, verbose_name="Nombre del programa", unique=True)
	codigo_programa = models.CharField(max_length=4,verbose_name="Codigo del programa", unique=True)
	facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
	estado = models.CharField(max_length=10, verbose_name="Estado", choices=ESTADOS, default='Activo')
	jornada = models.CharField(max_length=20, verbose_name="Jornada", choices=JORNADAS, default='Diurna')
	
	def __str__ (self):
		return self.nombre_programa