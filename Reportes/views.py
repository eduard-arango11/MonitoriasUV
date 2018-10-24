from django.shortcuts import render
from django.views.generic import TemplateView
from Usuarios.models import *
from ProgramasAcademicos.models import ProgramaAcademico
from OfertaMonitorias.models import OfertaMonitoria

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
        context['reportes'] = True
        context['reporte_estudiantes_registrados'] = True
        return context


class OfertasRegistradas(TemplateView):
    template_name = 'ofertas_registradas.html'

    def get_context_data(self, **kwargs):
        context = super(OfertasRegistradas, self).get_context_data(**kwargs)
        tipos_de_monitoria = ['Administrativa','Docencia','Investigacion','Especial']
        ofertas = []
        etiquetas = []
        for tipo in tipos_de_monitoria:
            etiquetas.append(tipo)
            cantidad_de_monitorias_de_este_tipo = OfertaMonitoria.objects.filter(tipo_monitoria=tipo,estado='Activo').count()
            ofertas.append(cantidad_de_monitorias_de_este_tipo)
        context['etiquetas'] = etiquetas
        context['ofertas'] = ofertas
        context['reportes'] = True
        context['reporte_monitorias_ofertadas'] = True
        return context