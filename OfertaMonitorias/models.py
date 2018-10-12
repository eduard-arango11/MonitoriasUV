from django.db import models
from Usuarios.models import Estudiante, Operario


TIPO_DE_MONITORIAS = (('Docencia','Docencia'),('Investigacion','Investigacion'),('Administrativa','Administrativa'),('Especial','Especial'))
SEDES = (('Melendez','Melendez'),('San Fernando','San Fernando'))
ESTADOS = (('Activo','Activo'),('Inactivo','Inactivo'))

class OfertaMonitoria(models.Model):
    perfil_requerido = models.CharField(max_length=800)
    tipo_monitoria = models.CharField(max_length=20, verbose_name="Tipo de Monitoria", choices=TIPO_DE_MONITORIAS, default='Administrativa')
    sede = models.CharField(max_length=20, verbose_name="Sede", choices=SEDES, default='Melendez')
    criterios_seleccion = models.CharField(max_length=800)
    periodo_duracion = models.CharField(max_length=200)
    horario_ejecucion = models.CharField(max_length=200)
    horas_semanales = models.PositiveIntegerField(verbose_name="Horas de trabajo semanales")
    plazo_solicitudes = models.DateField()
    fecha_seleccion = models.DateField()
    fecha_adjudicacion = models.DateField()
    resultado = models.CharField(max_length=800)
    estado = models.CharField(max_length=10, verbose_name="Estado", choices=ESTADOS, default='Activo')
    operario_registra = models.ForeignKey(Operario,on_delete=models.CASCADE)


    def __str__(self):
        return self.perfil_requerido

class AplicacionOferta(models.Model):
    oferta = models.ForeignKey(OfertaMonitoria, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10, verbose_name="Estado", choices=ESTADOS, default='Activo')

    def __str__(self):
        return self.oferta

    @staticmethod
    def obtenerAplicacionesEstudiante():
        return AplicacionOferta.objects.filter(estado='Activo')