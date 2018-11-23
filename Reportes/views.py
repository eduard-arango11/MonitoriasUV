from django.shortcuts import render
from django.views.generic import TemplateView
from Usuarios.models import *
from ProgramasAcademicos.models import ProgramaAcademico
from OfertaMonitorias.models import OfertaMonitoria
from OfertaMonitorias.models import AplicacionOferta
from Dependencias.models import Dependencia

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

        ############### REPORTE DE TIPOS DE MONITORIAS ###################
        tipos_de_monitoria = ['Administrativa','Docencia','Investigacion','Especial']
        ofertas = []
        etiquetas = []
        for tipo in tipos_de_monitoria:
            etiquetas.append(tipo)
            cantidad_de_monitorias_de_este_tipo = OfertaMonitoria.objects.filter(tipo_monitoria=tipo,estado='Activo').count()
            ofertas.append(cantidad_de_monitorias_de_este_tipo)
        context['etiquetas'] = etiquetas
        context['ofertas'] = ofertas

        ############### REPORTE DE MONITORIAS POR DEPENDENCIAS ###################
        dependencias = Dependencia.objects.all()
        ofertas_monitoria = OfertaMonitoria.objects.all()
        etiquetas_dependencias = []
        administrativa = []
        docencia = []
        investigacion = []
        especial = []
        for dependencia in dependencias:
            etiquetas_dependencias.append(dependencia.nombre)
            administrativa.append(OfertaMonitoria.objects.filter(operario_registra__dependencia=dependencia, estado='Activo',tipo_monitoria='Administrativa').count())
            docencia.append(OfertaMonitoria.objects.filter(operario_registra__dependencia=dependencia, estado='Activo',tipo_monitoria='Docencia').count())
            investigacion.append(OfertaMonitoria.objects.filter(operario_registra__dependencia=dependencia, estado='Activo',tipo_monitoria='Investigacion').count())
            especial.append(OfertaMonitoria.objects.filter(operario_registra__dependencia=dependencia, estado='Activo',tipo_monitoria='Especial').count())

        context['etiquetas_dependencias'] = etiquetas_dependencias
        context['administrativa'] = administrativa
        context['docencia'] = docencia
        context['investigacion'] = investigacion
        context['especial'] = especial
        context['reportes'] = True
        context['reporte_monitorias_ofertadas'] = True
        return context

class AplicacionesMonitorias(TemplateView):
    template_name = 'aplicaciones_monitorias.html'

    def get_context_data(self, **kwargs):
        context = super(AplicacionesMonitorias, self).get_context_data(**kwargs)

        tipos_de_monitoria = ['Administrativa', 'Docencia', 'Investigacion', 'Especial']
        ofertas = []
        for tipo in tipos_de_monitoria:
            cantidad_de_ofertas_de_este_tipo = OfertaMonitoria.objects.filter(tipo_monitoria=tipo,
                                                                                  estado='Activo').count()
            ofertas.append(cantidad_de_ofertas_de_este_tipo)

        context['ofertas'] = ofertas

        aplicaciones = []
        etiquetas = []
        for tipo in tipos_de_monitoria:
            etiquetas.append(tipo)
            cantidad_de_aplicaciones_de_este_tipo = AplicacionOferta.objects.filter(oferta__tipo_monitoria=tipo,
                                                                                 estado='Activo').count()
            aplicaciones.append(cantidad_de_aplicaciones_de_este_tipo)
        context['etiquetas'] = etiquetas
        context['aplicaciones'] = aplicaciones
        context['reportes'] = True
        context['reporte_aplicaciones_monitorias'] = True

        return context