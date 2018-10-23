from django.shortcuts import render
from django.views.generic import TemplateView
from Usuarios.models import *
from ProgramasAcademicos.models import ProgramaAcademico

class EstudiantesRegistrados(TemplateView):
    template_name = 'estudiantes_registrados.html'

    def get_context_data(self, **kwargs):
        context = super(EstudiantesRegistrados, self).get_context_data(**kwargs)
        programas = ProgramaAcademico.objects.all()
        hombres = []
        mujeres = []
        label = []
        cupos = []
        for programa in programas:
            label.append(programa.nombre_programa)
            estudiantes_hombres = Estudiante.objects.filter(programa_academico=programa,genero='Masculino').count()
            estudiantes_mujeres = Estudiante.objects.filter(programa_academico=programa,genero='Femenino').count()
            cupos2 = 20
            hombres.append(estudiantes_hombres)
            mujeres.append(estudiantes_mujeres)
            cupos.append(cupos2)
        context['label'] = label
        context['hombres'] = hombres
        context['mujeres'] = mujeres
        context['cupos'] = cupos
        return context