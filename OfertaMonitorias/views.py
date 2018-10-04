from django.db import transaction, IntegrityError
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import *
from Usuarios.models import *

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from monitorias.utilities import *
from datetime import date


class RegistrarOferta(SuccessMessageMixin, CreateView):
    model = OfertaMonitoria
    form_class = Formulario_registrar_oferta
    template_name = "registrar_oferta.html"
    success_url = reverse_lazy('registrar_oferta')
    success_message = "La oferta fue registrada exitosamente"

    def form_valid(self, form):
        operario = get_object_or_404(Operario, id=self.request.user.id)
        oferta = form.instance
        oferta.operario_registra=operario
        self.object = form.save()
        return super(RegistrarOferta, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RegistrarOferta, self).get_context_data(**kwargs)
        context['gestion_monitorias'] = True
        context['gestion_oferta'] = True
        context['registrar_oferta'] = True
        context['creacion'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Operario']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DetalleOferta(DetailView):
    model = OfertaMonitoria
    template_name = 'detalle_oferta.html'

class ListarOfertas(ListView):
    model = OfertaMonitoria
    template_name = "listar_ofertas.html"

    def get_queryset(self):
        queryset = super(ListarOfertas, self).get_queryset()

        if self.request.user.rol == 'Operario':
            operario = get_object_or_404(Operario, pk=self.request.user.id)
            queryset = queryset.filter(operario_registra=operario,estado='Activo')

        return queryset

    def get_context_data(self, **kwargs):
        if self.request.user.rol == 'Estudiante':
            estudiante = get_object_or_404(Estudiante, pk=self.request.user.id)
            aplicaciones_estudiante = AplicacionOferta.obtenerAplicacionesEstudiante().filter(estudiante=estudiante).values_list('oferta_id', flat=True)

        context = super(ListarOfertas, self).get_context_data(**kwargs)
        context['gestion_monitorias'] = True
        context['gestion_oferta'] = True
        context['listar_ofertas'] = True
        if self.request.user.rol == 'Estudiante':
            context['aplicaciones_estudiante'] = aplicaciones_estudiante
        return context


class RegistrarAplicacion(SuccessMessageMixin, CreateView):
    model = AplicacionOferta
    form_class = Formulario_registrar_aplicacion
    template_name = "registrar_aplicacion.html"
    success_url = reverse_lazy('registrar_aplicacion')
    success_message = "La aplicacion fue registrada exitosamente"

    def form_valid(self, form):
        self.object = form.save()
        return super(RegistrarAplicacion, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RegistrarAplicacion, self).get_context_data(**kwargs)
        context['gestion_monitorias'] = True
        context['gestion_aplicacion'] = True
        context['registrar_aplicacion'] = True
        context['creacion'] = True
        return context

class DetalleAplicacion(DetailView):
    model = AplicacionOferta
    template_name = 'detalle_aplicacion.html'

class ListarAplicaciones(ListView):
    model = AplicacionOferta
    template_name = "listar_aplicaciones.html"

    def get_queryset(self):
        queryset = super(ListarAplicaciones, self).get_queryset()

        if self.request.user.rol == 'Estudiante':
            estudiante = get_object_or_404(Estudiante, pk=self.request.user.id)
            queryset = queryset.filter(estudiante=estudiante,estado='Activo')

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListarAplicaciones, self).get_context_data(**kwargs)
        context['gestion_monitorias'] = True
        context['gestion_aplicacion'] = True
        context['listar_aplicaciones'] = True
        return context


def AplicarOferta(request,pk):
    estudiante = get_object_or_404(Estudiante, pk=request.user.id)
    oferta = get_object_or_404(OfertaMonitoria, pk=pk)
    try:
        aplicacion = AplicacionOferta.objects.get(oferta=oferta, estudiante=estudiante)
        aplicacion.estado = 'Activo'
        aplicacion.save()
    except AplicacionOferta.DoesNotExist:
        AplicacionOferta.objects.create(estudiante=estudiante, oferta=oferta)
    messages.success(request, 'Has aplicado a la oferta exitosamente')

    return redirect('listar_ofertas')

def cancelar_aplicacion(request, id_oferta):
    estudiante = get_object_or_404(Estudiante, pk=request.user.id)
    oferta = get_object_or_404(OfertaMonitoria, pk=id_oferta)
    aplicacion_para_cancelar = AplicacionOferta.obtenerAplicacionesEstudiante().filter(estudiante=estudiante).get(oferta=oferta)
    print(aplicacion_para_cancelar.id)
    aplicacion_para_cancelar.estado = 'Inactivo'
    aplicacion_para_cancelar.save()

    messages.success(request, 'La aplicacion a la oferta fue eliminada exitosamente')

    return redirect('listar_ofertas')

def RegistrarD10(request):
    estudiante = get_object_or_404(Estudiante, id=request.user.id)

    if request.method == 'POST':
        if D10.objects.all().filter(estudiante=estudiante):
            form_datos_basicos = Formulario_registrar_d10_datos_basicos(request.POST, instance=D10.objects.get(estudiante=estudiante).datos_basicos)
            form_datos_educacion = Formulario_registrar_d10_datos_educacion(request.POST, instance=D10.objects.get(estudiante=estudiante).datos_educacion)
            form_datos_capacitacion = Formulario_registrar_d10_datos_capacitacion(request.POST,instance=D10.objects.get(estudiante=estudiante).datos_capacitacion)
        else:
            form_datos_basicos = Formulario_registrar_d10_datos_basicos(request.POST)
            form_datos_educacion = Formulario_registrar_d10_datos_educacion(request.POST)
            form_datos_capacitacion = Formulario_registrar_d10_datos_capacitacion(request.POST)


        if form_datos_basicos.is_valid() and form_datos_educacion.is_valid() and form_datos_capacitacion.is_valid():
            try:
                with transaction.atomic():
                    if D10.objects.all().filter(estudiante=estudiante):
                        form_datos_educacion.save()
                        form_datos_capacitacion.save()
                        form_datos_basicos.save()
                    else:
                        obj_datos_basicos = form_datos_basicos.save()
                        obj_datos_educacion = form_datos_educacion.save()
                        obj_datos_capacitacion = form_datos_capacitacion.save()
                        D10.objects.create(estudiante=estudiante, datos_basicos=obj_datos_basicos,
                                       datos_educacion=obj_datos_educacion, datos_capacitacion=obj_datos_capacitacion)
                        estudiante.estado_d10='Registrado'
                        estudiante.save()
            except IntegrityError:
                messages.error(request, 'No se pudo guardar el d10')
            return redirect('listar_ofertas')
        else:
            messages.error(request, 'Por favor verificar los campos en rojo del formulario')
    else:
        if D10.objects.all().filter(estudiante=estudiante):
            print("else if")
            d10 = D10.objects.get(estudiante=estudiante)
            form_datos_basicos = Formulario_registrar_d10_datos_basicos(instance=d10.datos_basicos)
            form_datos_educacion = Formulario_registrar_d10_datos_educacion(instance=d10.datos_educacion)
            form_datos_capacitacion = Formulario_registrar_d10_datos_capacitacion(instance=d10.datos_capacitacion)
        else:
            print("else else")
            form_datos_basicos = Formulario_registrar_d10_datos_basicos()
            form_datos_educacion = Formulario_registrar_d10_datos_educacion()
            form_datos_capacitacion = Formulario_registrar_d10_datos_capacitacion()

    return render(request, 'registrar_d10.html', {
        'form_datos_basicos': form_datos_basicos,
        'form_datos_educacion': form_datos_educacion,
        'form_datos_capacitacion': form_datos_capacitacion,
        'registrar_formato_d10': True,
    })


class listarSolitudesAprobacionD10(ListView):
    model = D10
    template_name = "listar_solicitudes_d10.html"

    def get_queryset(self):
        queryset = super(listarSolitudesAprobacionD10, self).get_queryset()
        director = get_object_or_404(Director, pk=self.request.user.id)
        queryset = queryset.filter(estudiante__programa_academico__id=director.programa_academico.id).order_by('id')

        return queryset

    def get_context_data(self, **kwargs):
        context = super(listarSolitudesAprobacionD10, self).get_context_data(**kwargs)
        context['listar_solicitudes_d10'] = True
        return context

def revisarSolicitudAprobacionD10(request,id_d10):
    d10 = get_object_or_404(D10, id=id_d10)
    estudiante = d10.estudiante

    if request.method == 'POST':
        print("Hola desde POST")
        form_datos_basicos = Formulario_registrar_d10_datos_basicos(request.POST, instance=d10.datos_basicos)
        form_datos_educacion = Formulario_registrar_d10_datos_educacion(request.POST, instance=d10.datos_educacion)
        form_datos_capacitacion = Formulario_registrar_d10_datos_capacitacion(request.POST, instance=d10.datos_capacitacion)
        form_datos_aprobacion = Formulario_aprobar_d10(request.POST)

        if form_datos_basicos.is_valid() and form_datos_educacion.is_valid() and form_datos_capacitacion.is_valid() and form_datos_aprobacion.is_valid():
            d10.promedio_acumulado = form_datos_aprobacion.instance.promedio_acumulado
            d10.fecha_aprobacion = date.today()
            d10.estado_aprobacion = form_datos_aprobacion.instance.estado_aprobacion
            d10.save()

            return redirect('listar_solicitudes_d10')
        else:
            messages.error(request, 'Por favor verificar los campos en rojo del formulario')

    else:
        form_datos_basicos = Formulario_registrar_d10_datos_basicos(instance=d10.datos_basicos)
        form_datos_educacion = Formulario_registrar_d10_datos_educacion(instance=d10.datos_educacion)
        form_datos_capacitacion = Formulario_registrar_d10_datos_capacitacion(instance=d10.datos_capacitacion)
        form_datos_aprobacion = Formulario_aprobar_d10(instance=d10)

    return render(request, 'detalle_aprobacion_d10.html', {
        'form_datos_basicos': form_datos_basicos,
        'form_datos_educacion': form_datos_educacion,
        'form_datos_capacitacion': form_datos_capacitacion,
        'form_datos_aprobacion': form_datos_aprobacion,
        'd10': d10,
        'listar_solicitudes_d10': True,
    })