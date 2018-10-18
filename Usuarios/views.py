from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from monitorias.utilities import *
from django.shortcuts import get_object_or_404, render
from datetime import date
from django.db import transaction, IntegrityError


class RegistrarEstudiante(SuccessMessageMixin, CreateView):
    model = Estudiante
    form_class = Formulario_registrar_estudiante
    template_name = "registrar_estudiante.html"  # Se puede crear un template para todos los crear haciendo uso de context??
    success_url = reverse_lazy('registrar_estudiante')
    success_message = "El estudiante fue registrado exitosamente"

    def form_valid(self, form):
        estudiante = form.instance
        estudiante.username = estudiante.email
        estudiante.rol = "Estudiante"
        self.object = form.save()
        return super(RegistrarEstudiante, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RegistrarEstudiante, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_estudiantes'] = True
        context['registrar_estudiante'] = True
        context['creacion'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DetalleEstudiante(DetailView):
    model = Estudiante
    template_name = 'detalle_estudiante.html'

    def get_context_data(self, **kwargs):
        context = super(DetalleEstudiante, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_estudiantes'] = True
        context['listar_estudiantes'] = True
        return context


class ListarEstudiantes(ListView):
    model = Estudiante
    template_name = "listar_estudiantes.html"

    def get_queryset(self):
        queryset = super(ListarEstudiantes, self).get_queryset()
        queryset = queryset.order_by('-date_joined')

        if self.request.user.rol == 'Director':
            director = get_object_or_404(Director, pk=self.request.user.id)
            queryset = queryset.filter(programa_academico__id = director.programa_academico.id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListarEstudiantes, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_estudiantes'] = True
        context['listar_estudiantes'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Director', 'Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class EditarEstudiante(SuccessMessageMixin, UpdateView):
    model = Estudiante
    form_class = Formulario_modificar_estudiante
    template_name = "registrar_estudiante.html"
    success_url = reverse_lazy('listar_estudiantes')
    success_message = "El estudiante fue modificado exitosamente"

    def get_context_data(self, **kwargs):
        context = super(EditarEstudiante, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_estudiantes'] = True
        context['listar_estudiantes'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class RegistrarDirector(SuccessMessageMixin, CreateView):
    model = Director
    form_class = Formulario_registrar_director
    template_name = "registrar_director.html"  # Se puede crear un template para todos los crear haciendo uso de context??
    success_url = reverse_lazy('registrar_director')
    success_message = "El director de programa fue registrado exitosamente"

    def form_valid(self, form):
        director = form.instance
        director.username = director.email
        director.rol = "Director"
        self.object = form.save()
        return super(RegistrarDirector, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RegistrarDirector, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_directores'] = True
        context['registrar_director'] = True
        context['creacion'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DetalleDirector(DetailView):
    model = Director
    template_name = 'detalle_director.html'


class ListarDirectores(ListView):
    model = Director
    template_name = "listar_directores.html"

    def get_context_data(self, **kwargs):
        context = super(ListarDirectores, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_directores'] = True
        context['listar_directores'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador', 'Director', 'Operario', 'Estudiante']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class EditarDirector(SuccessMessageMixin, UpdateView):
    model = Director
    form_class = Formulario_modificar_director
    template_name = "registrar_director.html"
    success_url = reverse_lazy('listar_directores')
    success_message = "El director fue modificado exitosamente"

    def get_context_data(self, **kwargs):
        context = super(EditarDirector, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_directores'] = True
        context['listar_directores'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class RegistrarOperario(SuccessMessageMixin, CreateView):
    model = Operario
    form_class = Formulario_registrar_operario
    template_name = "registrar_operario.html"  # Se puede crear un template para todos los crear haciendo uso de context??
    success_url = reverse_lazy('registrar_operario')
    success_message = "El operario fue registrado exitosamente"

    def form_valid(self, form):
        operario = form.instance
        operario.username = operario.email
        operario.rol = "Operario"
        self.object = form.save()
        return super(RegistrarOperario, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RegistrarOperario, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_operarios'] = True
        context['registrar_operario'] = True
        context['creacion'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DetalleOperario(DetailView):
    model = Operario
    template_name = 'detalle_operario.html'


class ListarOperarios(ListView):
    model = Operario
    template_name = "listar_operarios.html"

    def get_context_data(self, **kwargs):
        context = super(ListarOperarios, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_operarios'] = True
        context['listar_operarios'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class EditarOperario(SuccessMessageMixin, UpdateView):
    model = Operario
    form_class = Formulario_modificar_operario
    template_name = "registrar_operario.html"
    success_url = reverse_lazy('listar_operarios')
    success_message = "El operario fue modificado exitosamente"

    def get_context_data(self, **kwargs):
        context = super(EditarOperario, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_operarios'] = True
        context['listar_operarios'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class RegistrarAdministrador(SuccessMessageMixin, CreateView):
    model = Administrador
    form_class = Formulario_registrar_administrador
    template_name = "registrar_administrador.html"  # Se puede crear un template para todos los crear haciendo uso de context??
    success_url = reverse_lazy('registrar_administrador')
    success_message = "El administrador fue registrado exitosamente"

    def form_valid(self, form):
        administrador = form.instance
        administrador.username = administrador.email
        administrador.rol = "Administrador"
        self.object = form.save()
        return super(RegistrarAdministrador, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RegistrarAdministrador, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_administradores'] = True
        context['registrar_administrador'] = True
        context['creacion'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DetalleAdministrador(DetailView):
    model = Administrador
    template_name = 'detalle_administrador.html'


class ListarAdministradores(ListView):
    model = Administrador
    template_name = "listar_administradores.html"

    def get_context_data(self, **kwargs):
        context = super(ListarAdministradores, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_administradores'] = True
        context['listar_administradores'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class EditarAdministrador(SuccessMessageMixin, UpdateView):
    model = Administrador
    form_class = Formulario_modificar_administrador
    template_name = "registrar_administrador.html"
    success_url = reverse_lazy('listar_administradores')
    success_message = "El administrador fue modificado exitosamente"

    def get_context_data(self, **kwargs):
        context = super(EditarAdministrador, self).get_context_data(**kwargs)
        context['gestion_usuarios'] = True
        context['gestion_administradores'] = True
        context['listar_administradores'] = True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def RegistrarD10(request):

    if request.user.rol != 'Estudiante':
        return render(request, '404.html')

    estudiante = get_object_or_404(Estudiante, id=request.user.id)
    accion = 'Registro'

    if request.method == 'POST':
        if estudiante.d10:
            print("D10 Actualizado")
            form_datos_basicos = Formulario_registrar_d10_datos_basicos(request.POST, instance=D10.objects.get(
                estudiante=estudiante).datos_basicos)
            form_datos_educacion = Formulario_registrar_d10_datos_educacion(request.POST, instance=D10.objects.get(
                estudiante=estudiante).datos_educacion)
            form_datos_capacitacion = Formulario_registrar_d10_datos_capacitacion(request.POST,
                                                                                  instance=D10.objects.get(
                                                                                      estudiante=estudiante).datos_capacitacion)
        else:
            print("D10 Registrado")
            form_datos_basicos = Formulario_registrar_d10_datos_basicos(request.POST)
            form_datos_educacion = Formulario_registrar_d10_datos_educacion(request.POST)
            form_datos_capacitacion = Formulario_registrar_d10_datos_capacitacion(request.POST)

        if form_datos_basicos.is_valid() and form_datos_educacion.is_valid() and form_datos_capacitacion.is_valid():
            try:
                with transaction.atomic():
                    if estudiante.d10:
                        form_datos_educacion.save()
                        form_datos_capacitacion.save()
                        form_datos_basicos.save()
                        messages.success(request, 'Se ha actualizado existosamente su D10')
                    else:
                        obj_datos_basicos = form_datos_basicos.save()
                        obj_datos_educacion = form_datos_educacion.save()
                        obj_datos_capacitacion = form_datos_capacitacion.save()
                        d10_estudiante = D10.objects.create(datos_basicos=obj_datos_basicos,
                                                            datos_educacion=obj_datos_educacion,
                                                            datos_capacitacion=obj_datos_capacitacion)
                        estudiante.d10 = d10_estudiante
                        estudiante.estado_d10 = 'Registrado'
                        estudiante.save()
                        messages.success(request, 'Se ha registrado existosamente su D10')
            except IntegrityError:
                messages.error(request, 'No se pudo guardar el d10')
            return redirect('listar_ofertas')
        else:
            messages.error(request, 'Por favor verificar los campos en rojo del formulario')
    else:
        if estudiante.d10:
            accion = 'Actualizacion'
            print("El estudiante tiene D10")
            form_datos_basicos = Formulario_registrar_d10_datos_basicos(instance=estudiante.d10.datos_basicos)
            form_datos_educacion = Formulario_registrar_d10_datos_educacion(instance=estudiante.d10.datos_educacion)
            form_datos_capacitacion = Formulario_registrar_d10_datos_capacitacion(
                instance=estudiante.d10.datos_capacitacion)
        else:
            accion = 'Registro'
            print("El estudiante NO tiene D10")
            form_datos_basicos = Formulario_registrar_d10_datos_basicos()
            form_datos_educacion = Formulario_registrar_d10_datos_educacion()
            form_datos_capacitacion = Formulario_registrar_d10_datos_capacitacion()

    return render(request, 'registrar_d10.html', {
        'form_datos_basicos': form_datos_basicos,
        'form_datos_educacion': form_datos_educacion,
        'form_datos_capacitacion': form_datos_capacitacion,
        'registrar_formato_d10': True,
        'accion': accion,
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

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Director']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def revisarSolicitudAprobacionD10(request, id_d10):
    d10 = get_object_or_404(D10, id=id_d10)
    estudiante = d10.estudiante

    if request.user.rol != 'Director':
        return render(request, '404.html')

    if Director.objects.get(id=request.user.id).programa_academico.id != estudiante.programa_academico.id:
        return render(request, '404.html')

    if request.method == 'POST':
        print("Hola desde POST")
        form_datos_basicos = Formulario_registrar_d10_datos_basicos(request.POST, instance=d10.datos_basicos)
        form_datos_educacion = Formulario_registrar_d10_datos_educacion(request.POST, instance=d10.datos_educacion)
        form_datos_capacitacion = Formulario_registrar_d10_datos_capacitacion(request.POST,
                                                                              instance=d10.datos_capacitacion)
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
