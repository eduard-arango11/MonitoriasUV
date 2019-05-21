from django.views.generic import *
from Facultades.models import Facultad
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from monitorias.utilities import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages


class RegistrarFacultad(SuccessMessageMixin, CreateView):
    model = Facultad
    form_class = Formulario_registrar_facultad
    template_name = "registrar_facultad.html"
    success_url = reverse_lazy('registrar_facultad')
    success_message = "La facultad fue registrada exitosamente"

    def form_valid (self, form):
        self.object = form.save()
        return super(RegistrarFacultad, self).form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super(RegistrarFacultad, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_facultades'] = True
        context['registrar_facultad']= True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ListarFacultades(ListView):
    model = Facultad
    template_name = "listar_facultades.html"

    def get_context_data(self, **kwargs):
        context = super(ListarFacultades, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_facultades'] = True
        context['listar_facultades']= True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class EditarFacultad(SuccessMessageMixin, UpdateView):
    model = Facultad
    form_class = Formulario_registrar_facultad
    template_name = "registrar_facultad.html"
    success_url = reverse_lazy('listar_facultades')
    success_message = "La facultad fue modificada exitosamente"
    
    def get_context_data(self, **kwargs):
        context = super(EditarFacultad, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_facultades'] = True
        context['listar_facultades']= True
        return context

    @method_decorator(login_required)
    @method_decorator(verificar_rol(roles_permitidos=['Administrador']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def eliminar_facultad(request):
    id = request.GET.get('id', '')
    mi_objeto = get_object_or_404(Facultad, pk=id)
    mi_objeto.delete()
    messages.success(request, 'Facultad eliminada con exito')
    data = {
        'eliminacion': True,
    }
    return JsonResponse(data)
