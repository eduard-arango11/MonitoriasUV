from django.db import models
from Usuarios.models import Estudiante, Operario


TIPO_DE_MONITORIAS = (('Docencia','Docencia'),('Investigacion','Investigacion'),('Administrativa','Administrativa'),('Especial','Especial'))
SEDES = (('Melendez','Melendez'),('San Fernando','San Fernando'))
ESTADOS = (('Activo','Activo'),('Inactivo','Inactivo'))
ESTADOS_APROBACION = (('En Revision','En Revision'),('Aprobado','Aprobado'),('No Aprobado','No Aprobado'))
TIPOS_ESTADO_CIVIL = (('Soltero','Soltero'),('Casado','Casado'),('Union Libre','Union Libre'),('Otro','Otro'))
TIPO_POSICION_FAMILIAR = (('Hijo(a)','Hijo(a)'),('Independiente','Independiente'),('Cabeza de familia','Cabeza de familia'),('Esposo(a)','Esposo(a)'))

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

class DatosBasicosD10(models.Model):
    semestre = models.CharField(max_length=2,verbose_name="Semestre",blank=True)
    estado_civil = models.CharField(max_length=20, verbose_name="Estado civil", choices=TIPOS_ESTADO_CIVIL, default='Soltero',blank=True)
    numero_de_personas_a_cargo = models.CharField(max_length=2,verbose_name="Numero de personas a su cargo",blank=True)
    posicion_familiar = models.CharField(max_length=50,verbose_name="Posicion familiar", choices=TIPO_POSICION_FAMILIAR, default='Hijo(a)',blank=True)
    direccion_residencia = models.CharField(max_length=50,verbose_name="Direccion actual de residencia",blank=True)
    estrato = models.CharField(max_length=2,verbose_name="Estrato",blank=True)
    barrio = models.CharField(max_length=50,verbose_name="Barrio",blank=True)
    ciudad = models.CharField(max_length=50,verbose_name="Ciudad",blank=True)
    departamento = models.CharField(max_length=50,verbose_name="Departamento",blank=True)
    nombre_acudiente = models.CharField(max_length=300,verbose_name="Nombre de una persona que le de informacion",blank=True)
    telefono_acudiente = models.CharField(max_length=10,verbose_name="Telefono de persona que le de informacion",blank=True)
    perfil_ocupacional = models.CharField(max_length=800,blank=True)
    sistemas_que_maneja = models.CharField(max_length=800,blank=True)

class DatosEducacionD10(models.Model):
    titulo_obtenido_bachillerato = models.CharField(max_length=50,verbose_name="Titulo obtenido",blank=True)
    ano_finalizacion_bachillerato = models.CharField(max_length=4,verbose_name="Año de finalizacion bachiller",blank=True)
    nombre_colegio_bachillerato = models.CharField(max_length=50,verbose_name="Nombre del establecimiento",blank=True)
    ciudad_colegio_bachillerato = models.CharField(max_length=50,verbose_name="Cuidad",blank=True)
    semestres_otros_estudios = models.CharField(max_length=2,verbose_name="Semestres",blank=True)
    plan_otros_estudios = models.CharField(max_length=50,verbose_name="Plan de estudios o titulo obtenido",blank=True)
    ano_finalizacion_otros_estudios = models.CharField(max_length=4,verbose_name="Año de finalizacion",blank=True)
    nombre_establecimiento_otros_estudios = models.CharField(max_length=50,verbose_name="Nombre del establecimiento",blank=True)
    ciudad_establecimiento_otros_estudios = models.CharField(max_length=30,verbose_name="Ciudad",blank=True)

class DatosCapacitacionD10(models.Model):
    nombre_establecimiento = models.CharField(max_length=50,verbose_name="Nombre del establecimiento",blank=True)
    nombre_curso = models.CharField(max_length=50,verbose_name="Nombre del curso",blank=True)
    duracion_cruso = models.CharField(max_length=4,verbose_name="Duracion del curso (horas)",blank=True)
    fecha_finalizacion_curso = models.DateField(null=True, blank=True)

class D10(models.Model):
    estado = models.CharField(max_length=10, verbose_name="Estado", choices=ESTADOS, default='Activo')
    estado_aprobacion = models.CharField(max_length=20, verbose_name="Estado Aprobacion", choices=ESTADOS_APROBACION, default='En Revision')
    datos_basicos = models.OneToOneField(DatosBasicosD10, on_delete=models.CASCADE)
    datos_educacion = models.OneToOneField(DatosEducacionD10, on_delete=models.CASCADE)
    datos_capacitacion = models.OneToOneField(DatosCapacitacionD10, on_delete=models.CASCADE)
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)