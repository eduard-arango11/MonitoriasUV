from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from Usuarios.models import *
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from monitorias.utilities import *
from datetime import datetime

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


class EditarOferta(SuccessMessageMixin, UpdateView):
    model = OfertaMonitoria
    form_class = Formulario_registrar_oferta
    template_name = "registrar_oferta.html"
    success_url = reverse_lazy('listar_ofertas')
    success_message = "La oferta fue modificada exitosamente"

    def get_context_data(self, **kwargs):
        context = super(EditarOferta, self).get_context_data(**kwargs)
        context['gestion_monitorias'] = True
        context['gestion_oferta'] = True
        context['registrar_oferta'] = True
        context['creacion'] = False
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Operario']))
    @method_decorator(verificar_operario_propietario_de_oferta())
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
            queryset = queryset.filter(operario_registra=operario)

        if self.request.user.rol == 'Estudiante':
            queryset = OfertaMonitoria.obtenerOfertasActivas()

        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        if self.request.user.rol == 'Estudiante':
            estudiante = get_object_or_404(Estudiante, pk=self.request.user.id)
            aplicaciones_estudiante = AplicacionOferta.obtenerAplicacionesEstudiante().filter(estudiante=estudiante).values_list('oferta_id', flat=True)

        context = super(ListarOfertas, self).get_context_data(**kwargs)
        context['gestion_monitorias'] = True
        context['gestion_oferta'] = True
        context['listar_ofertas'] = True
        context['time'] = datetime.now().date().isoformat()
        if self.request.user.rol == 'Estudiante':
            context['aplicaciones_estudiante'] = aplicaciones_estudiante
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
            if estudiante.estado_d10 == 'Registrado' and estudiante.d10.estado_aprobacion == 'En Revision':
                queryset = queryset.filter(estudiante=estudiante, estado='D10 en revision')
            else:
                queryset = queryset.filter(estudiante=estudiante, estado='Activo')

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListarAplicaciones, self).get_context_data(**kwargs)
        context['gestion_monitorias'] = True
        context['gestion_aplicacion'] = True
        context['listar_aplicaciones'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Estudiante','Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def AplicarOferta(request,pk):
    estudiante = get_object_or_404(Estudiante, pk=request.user.id)
    oferta = get_object_or_404(OfertaMonitoria, pk=pk)
    try:
        aplicacion = AplicacionOferta.objects.get(oferta=oferta, estudiante=estudiante)
        if estudiante.d10.estado_aprobacion == 'En Revision':
            aplicacion.estado = 'D10 en revision'
            aplicacion.save()
            messages.warning(request,'Aplicacion exitosa: Cuando tu director de programa apruebe tu D10 la aplicacion a la oferta se completara automaticamente')
        elif estudiante.d10.estado_aprobacion == 'Aprobado':
            aplicacion.estado = 'Activo'
            aplicacion.save()
            messages.success(request, 'Has aplicado a la oferta exitosamente')
    except AplicacionOferta.DoesNotExist:
        if estudiante.d10.estado_aprobacion == 'En Revision':
            AplicacionOferta.objects.create(estudiante=estudiante, oferta=oferta, estado='D10 en revision')
            messages.warning(request, 'Aplicacion exitosa: Cuando tu director de programa apruebe tu D10 la aplicacion a la oferta se completara automaticamente')
        elif estudiante.d10.estado_aprobacion == 'Aprobado':
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

def listar_aplicaciones_oferta(request, id_oferta):
    operario = get_object_or_404(Operario, pk=request.user.id)
    oferta = get_object_or_404(OfertaMonitoria, pk=id_oferta)
    aplicaciones = AplicacionOferta.objects.filter(oferta__operario_registra=operario, oferta=oferta, estado='Activo')

    if oferta.operario_registra.id != operario.id:
        return render(request, '404.html')

    return render(request, 'listar_aplicaciones_oferta.html', {
        'aplicaciones': aplicaciones,
        'oferta': oferta,
        'gestion_monitorias': True,
        'gestion_oferta': True,
        'listar_ofertas': True,
    })

def listar_estudiantes_d10(request):
    if request.user.rol != 'Operario':
        return render(request, '404.html')

    estudiantes = Estudiante.objects.filter(estado_d10='Registrado',estado='Activo',d10__estado_aprobacion='Aprobado').order_by('-d10__promedio_acumulado')

    return render(request, 'listar_estudiantes_con_d10.html', {
        'object_list': estudiantes,
        'estudiantes_con_d10': True,
    })