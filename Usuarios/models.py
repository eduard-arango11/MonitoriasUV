from django.db import models
from django.contrib.auth.models import AbstractUser
from ProgramasAcademicos.models import *
from datetime import date

TIPOS_DE_IDENTIFICACION = (('CC','Cedula de Ciudadania'),('TI','Tarjeta de Identidad'),('CE','Cedula Extranjera'))
GENEROS = (('Masculino','Masculino'),('Femenino','Femenino'))
ROLES = (('Estudiante','Estudiante'),('Director','Director'),('Operario','Operario'),('Administrador','Administrador'))
ESTADOS = (('Activo','Activo'),('Inactivo','Inactivo'))
ESTADOS_D10 = (('No registrado','No registrado'),('Registrado','Registrado'))


ESTADOS_APROBACION = (('En Revision','En Revision'),('Aprobado','Aprobado'),('No Aprobado','No Aprobado'))
TIPOS_ESTADO_CIVIL = (('Soltero','Soltero'),('Casado','Casado'),('Union Libre','Union Libre'),('Otro','Otro'))
TIPO_POSICION_FAMILIAR = (('Hijo(a)','Hijo(a)'),('Independiente','Independiente'),('Cabeza de familia','Cabeza de familia'),('Esposo(a)','Esposo(a)'))

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

OPCIONES_NIVEL_IDIOMA = (('Muy Bueno','Muy Bueno'),('Bueno','Bueno'),('Regular','Regular'))

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
    idioma_nombre = models.CharField(max_length=30,verbose_name="Idioma",blank=True)
    idioma_nivel_habla = models.CharField(max_length=20, verbose_name="Habla", choices=OPCIONES_NIVEL_IDIOMA,blank=True)
    idioma_nivel_escribe = models.CharField(max_length=20, verbose_name="Escribe", choices=OPCIONES_NIVEL_IDIOMA,blank=True)
    idioma_nivel_lee = models.CharField(max_length=20, verbose_name="Lee", choices=OPCIONES_NIVEL_IDIOMA,blank=True)

class DatosCapacitacionD10(models.Model):
    nombre_establecimiento = models.CharField(max_length=50,verbose_name="Nombre del establecimiento",blank=True)
    nombre_curso = models.CharField(max_length=50,verbose_name="Nombre del curso",blank=True)
    duracion_cruso = models.CharField(max_length=4,verbose_name="Duracion del curso (horas)",blank=True)
    fecha_finalizacion_curso = models.DateField(null=True, blank=True)

class DatosExperienciaLaboralD10(models.Model):
    nombre_empresa = models.CharField(max_length=100,verbose_name="Nombre del establecimiento",blank=True)
    cargo = models.CharField(max_length=80,verbose_name="Cargo desempeñado",blank=True)
    funciones_realizadas = models.CharField(max_length=800,verbose_name="Funciones realizadas",blank=True)
    logros = models.CharField(max_length=800,verbose_name="Logros",blank=True)
    jefe_inmediato = models.CharField(max_length=200,verbose_name="Nombre del jefe inmediato",blank=True)
    cargo_jefe = models.CharField(max_length=80,verbose_name="Cargo del jefe inmediato",blank=True)
    telefono_empresa = models.CharField(max_length=10,verbose_name="Telefono de la empresa",blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_finalizacion = models.DateField(null=True, blank=True)


class DatosHorarioDisponibleD10(models.Model):
    lunes_inicio_1 = models.CharField(max_length=30,null=True, blank=True)
    lunes_fin_1 = models.CharField(max_length=30,null=True, blank=True)
    lunes_inicio_2 = models.CharField(max_length=30,null=True, blank=True)
    lunes_fin_2 = models.CharField(max_length=30,null=True, blank=True)
    lunes_inicio_3 = models.CharField(max_length=30,null=True, blank=True)
    lunes_fin_3 = models.CharField(max_length=30,null=True, blank=True)
    martes_inicio_1 = models.CharField(max_length=30,null=True, blank=True)
    martes_fin_1 = models.CharField(max_length=30,null=True, blank=True)
    martes_inicio_2 = models.CharField(max_length=30,null=True, blank=True)
    martes_fin_2 = models.CharField(max_length=30,null=True, blank=True)
    martes_inicio_3 = models.CharField(max_length=30,null=True, blank=True)
    martes_fin_3 = models.CharField(max_length=30,null=True, blank=True)
    miercoles_inicio_1 = models.CharField(max_length=30,null=True, blank=True)
    miercoles_fin_1 = models.CharField(max_length=30,null=True, blank=True)
    miercoles_inicio_2 = models.CharField(max_length=30,null=True, blank=True)
    miercoles_fin_2 = models.CharField(max_length=30,null=True, blank=True)
    miercoles_inicio_3 = models.CharField(max_length=30,null=True, blank=True)
    miercoles_fin_3 = models.CharField(max_length=30,null=True, blank=True)
    jueves_inicio_1 = models.CharField(max_length=30,null=True, blank=True)
    jueves_fin_1 = models.CharField(max_length=30,null=True, blank=True)
    jueves_inicio_2 = models.CharField(max_length=30,null=True, blank=True)
    jueves_fin_2 = models.CharField(max_length=30,null=True, blank=True)
    jueves_inicio_3 = models.CharField(max_length=30,null=True, blank=True)
    jueves_fin_3 = models.CharField(max_length=30,null=True, blank=True)
    viernes_inicio_1 = models.CharField(max_length=30,null=True, blank=True)
    viernes_fin_1 = models.CharField(max_length=30,null=True, blank=True)
    viernes_inicio_2 = models.CharField(max_length=30,null=True, blank=True)
    viernes_fin_2 = models.CharField(max_length=30,null=True, blank=True)
    viernes_inicio_3 = models.CharField(max_length=30,null=True, blank=True)
    viernes_fin_3 = models.CharField(max_length=30,null=True, blank=True)
    sabado_inicio_1 = models.CharField(max_length=30,null=True, blank=True)
    sabado_fin_1 = models.CharField(max_length=30,null=True, blank=True)
    sabado_inicio_2 = models.CharField(max_length=30,null=True, blank=True)
    sabado_fin_2 = models.CharField(max_length=30,null=True, blank=True)
    sabado_inicio_3 = models.CharField(max_length=30,null=True, blank=True)
    sabado_fin_3 = models.CharField(max_length=30,null=True, blank=True)
    domingo_inicio_1 = models.CharField(max_length=30,null=True, blank=True)
    domingo_fin_1 = models.CharField(max_length=30,null=True, blank=True)
    domingo_inicio_2 = models.CharField(max_length=30,null=True, blank=True)
    domingo_fin_2 = models.CharField(max_length=30,null=True, blank=True)
    domingo_inicio_3 = models.CharField(max_length=30,null=True, blank=True)
    domingo_fin_3 = models.CharField(max_length=30,null=True, blank=True)


class D10(models.Model):
    estado = models.CharField(max_length=10, verbose_name="Estado", choices=ESTADOS, default='Activo')
    estado_aprobacion = models.CharField(max_length=20, verbose_name="Estado Aprobacion", choices=ESTADOS_APROBACION, default='En Revision')
    datos_basicos = models.OneToOneField(DatosBasicosD10, on_delete=models.CASCADE)
    datos_educacion = models.OneToOneField(DatosEducacionD10, on_delete=models.CASCADE)
    datos_capacitacion = models.OneToOneField(DatosCapacitacionD10, on_delete=models.CASCADE)
    datos_experiencia_laboral = models.OneToOneField(DatosExperienciaLaboralD10, on_delete=models.CASCADE)
    datos_horario_disponible = models.OneToOneField(DatosHorarioDisponibleD10, on_delete=models.CASCADE)
    promedio_acumulado = models.CharField(max_length=5,verbose_name="Promedio Acumulado del Estudiante",blank=True)
    fecha_aprobacion = models.DateField(null=True, blank=True)

class Usuario(AbstractUser):
    nombres = models.CharField(max_length=300,verbose_name="Nombre(s)")
    primer_apellido = models.CharField(max_length=100,verbose_name="Primer apellido")
    segundo_apellido = models.CharField(max_length=100,verbose_name="Segundo apellido")
    tipo_documento = models.CharField(max_length=2,verbose_name="Tipo de documento",choices = TIPOS_DE_IDENTIFICACION)
    numero_documento = models.CharField(max_length=20,verbose_name="Numero de documento", unique=True)
    lugar_expedicion_documento = models.CharField(max_length=200, verbose_name="Lugar de expedicion")
    telefono = models.CharField(max_length=10,verbose_name="Telefono de contacto")
    genero = models.CharField(max_length=20, verbose_name="Genero", choices=GENEROS)
    lugar_nacimiento = models.CharField(max_length=200, verbose_name="Lugar de nacimiento")
    fecha_nacimiento = models.DateField()
    rol = models.CharField(max_length=30, verbose_name="Rol", choices=ROLES)
    estado = models.CharField(max_length=10, verbose_name="Estado", choices=ESTADOS, default='Activo')

    def nombreCompleto(self):
        nombre_completo = self.nombres +" "+ self.primer_apellido
        if self.segundo_apellido != '':
            nombre_completo= nombre_completo +" "+ self.segundo_apellido
        return nombre_completo

    def numeroTelefonico(self):
        if len(self.telefono) == 10:
            return self.telefono[0:3] + " " + self.telefono[3:6] + " " + self.telefono[6:8] + " " + self.telefono[8:10]
        else:
            return self.telefono[0:3] + " " + self.telefono[3:5] + " " + self.telefono[5:7]

    def edad(self):
        return date.today().year - self.fecha_nacimiento.year

class Estudiante(Usuario):
    codigo = models.CharField(max_length=7,verbose_name="Codigo de estudiante", unique=True)
    programa_academico = models.ForeignKey(ProgramaAcademico, on_delete=models.CASCADE)
    estado_d10 = models.CharField(max_length=20, verbose_name="Estado d10", choices=ESTADOS_D10, default='No registrado')
    d10 = models.OneToOneField(D10, on_delete=models.CASCADE, null=True, blank=True)

class Director(Usuario):
    programa_academico = models.ForeignKey(ProgramaAcademico, on_delete=models.CASCADE)

class Operario(Usuario):
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    dependencia = models.CharField(max_length=100, verbose_name="Dependencia")

class Administrador(Usuario):
    pass