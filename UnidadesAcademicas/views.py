from django.views.generic import *
from UnidadesAcademicas.models import Unidad
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from monitorias.utilities import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class RegistrarUnidad(SuccessMessageMixin, CreateView):
    model = Unidad
    form_class = Formulario_registrar_unidad
    template_name = "registrar_unidad.html"
    success_url = reverse_lazy('registrar_unidad')
    success_message = "La unidad academica fue registrada exitosamente"

    def form_valid (self, form):
        self.object = form.save()
        return super(RegistrarUnidad, self).form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super(RegistrarUnidad, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_unidades'] = True
        context['registrar_unidad']= True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ListarUnidades(ListView):
    model = Unidad
    template_name = "listar_unidades.html"

    def get_context_data(self, **kwargs):
        context = super(ListarUnidades, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_unidades'] = True
        context['listar_unidades']= True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class EditarUnidad(SuccessMessageMixin, UpdateView):
    model = Unidad
    form_class = Formulario_registrar_unidad
    template_name = "registrar_unidad.html"
    success_url = reverse_lazy('listar_unidades')
    success_message = "La unidad academica fue modificada exitosamente"
    
    def get_context_data(self, **kwargs):
        context = super(EditarUnidad, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_unidades'] = True
        context['listar_unidades']= True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def eliminar_unidad(request):
    id = request.GET.get('id', '')
    mi_objeto = get_object_or_404(Unidad, pk=id)
    mi_objeto.delete()
    data = {
        'eliminacion': True,
    }
    return JsonResponse(data)