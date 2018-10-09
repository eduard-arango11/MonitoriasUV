from django.db import models
from django.contrib.auth.models import AbstractUser
from ProgramasAcademicos.models import *
from datetime import date

TIPOS_DE_IDENTIFICACION = (('CC','Cedula de Ciudadania'),('TI','Tarjeta de Identidad'),('CE','Cedula Extranjera'))
GENEROS = (('Masculino','Masculino'),('Femenino','Femenino'))
ROLES = (('Estudiante','Estudiante'),('Director','Director'),('Operario','Operario'),('Administrador','Administrador'))
ESTADOS = (('Activo','Activo'),('Inactivo','Inactivo'))
ESTADOS_D10 = (('No registrado','No registrado'),('Registrado','Registrado'))


class Usuario(AbstractUser):
    nombres = models.CharField(max_length=300,verbose_name="Nombre(s)")
    primer_apellido = models.CharField(max_length=100,verbose_name="Primer apellido")
    segundo_apellido = models.CharField(max_length=100,verbose_name="Segundo apellido")
    tipo_documento = models.CharField(max_length=2,verbose_name="Tipo de documento",choices = TIPOS_DE_IDENTIFICACION)
    numero_documento = models.CharField(max_length=20,verbose_name="Numero de documento", unique=True)
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

class Director(Usuario):
    programa_academico = models.ForeignKey(ProgramaAcademico, on_delete=models.CASCADE)

class Operario(Usuario):
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    dependencia = models.CharField(max_length=100, verbose_name="Dependencia")

class Administrador(Usuario):
    pass

