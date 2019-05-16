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

        ######### TOTAL DE ESTUDIANTES ########

        total_estudiantes = Estudiante.objects.filter(estado='Activo').count()
        context['total_estudiantes'] = total_estudiantes

        ######### TOTAL DE ESTUDIANTES SIN D10 ########

        total_estudiantes_sin_d10 = Estudiante.objects.filter(estado='Activo', estado_d10='No registrado').count()
        context['total_estudiantes_sin_d10'] = total_estudiantes_sin_d10

        ######### TOTAL DE ESTUDIANTES CON D10 REGISTRADOS ########

        total_estudiantes_d10_registrado = Estudiante.objects.filter(estado='Activo', estado_d10='Registrado').count()
        context['total_estudiantes_d10_registrado'] = total_estudiantes_d10_registrado

        ######### TOTAL DE ESTUDIANTES CON D10 REGISTRADOS ########

        total_estudiantes_d10_aprobado = Estudiante.objects.filter(estado='Activo', estado_d10='Registrado', d10__estado_aprobacion='Aprobado').count()
        context['total_estudiantes_d10_aprobado'] = total_estudiantes_d10_aprobado


        context['reportes'] = True
        context['reporte_estudiantes_registrados'] = True
        return context


class OfertasRegistradas(TemplateView):
    template_name = 'ofertas_registradas.html'

    def get_context_data(self, **kwargs):
        context = super(OfertasRegistradas, self).get_context_data(**kwargs)

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

        ################## REPORTE DE MONITORIAS POR TIPO DE OFERTA Y POR ESTADO DE LA OFERTA #####

        #programas = ProgramaAcademico.objects.all()
        #ofertas = OfertaMonitoria.objects.all()
        tipos_oferta = ['Docencia','Investigacion','Administrativa','Especial']
        activas = []
        terminadas = []
        #label = []
        #cupos = []
        for tipo in tipos_oferta:
            #label.append(tipo)
            activas_oferta = OfertaMonitoria.objects.filter(tipo_monitoria=tipo,estado='Activo').count()
            terminadas_oferta = OfertaMonitoria.objects.filter(tipo_monitoria=tipo,estado='Terminada').count()
            activas.append(activas_oferta)
            terminadas.append(terminadas_oferta)
        context['tipos_oferta'] = tipos_oferta
        context['activas'] = activas
        context['terminadas'] = terminadas

        ######### TOTAL DE OFERTAS ########

        total_ofertas = OfertaMonitoria.objects.filter(estado='Activo').count() + OfertaMonitoria.objects.filter(estado='Terminada').count()
        context['total_ofertas'] = total_ofertas

        ######### TOTAL DE OFERTAS EN PROCESO ########

        total_ofertas_en_proceso = OfertaMonitoria.objects.filter(estado='Activo').count()
        context['total_ofertas_en_proceso'] = total_ofertas_en_proceso

        ######### TOTAL DE OFERTAS TERMINADAS ########

        total_ofertas_terminadas = OfertaMonitoria.objects.filter(estado='Terminada').count()
        context['total_ofertas_terminadas'] = total_ofertas_terminadas

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

        ############## PROMEDIO DE APLICACIONES POR OFERTA #############

        promedio = 0
        print("promedio: " + str(promedio))
        for tipo in tipos_de_monitoria:
            cantidad_de_aplicaciones_de_este_tipo = AplicacionOferta.objects.filter(oferta__tipo_monitoria=tipo,
                                                                                    estado='Activo').count()
            print("cantidad_de_aplicaciones_de_este_tipo: " + str(cantidad_de_aplicaciones_de_este_tipo))

        context['reportes'] = True
        context['reporte_aplicaciones_monitorias'] = True

        ############## TOTAL DE APLICACIONES ################

        context['total_aplicaciones'] = AplicacionOferta.objects.all().count()
        context['total_aplicaciones_en_proceso'] = AplicacionOferta.objects.filter(estado='Activo').count()
        context['total_aplicaciones_terminadas'] = AplicacionOferta.objects.filter(estado='Aprobada').count()


        return context