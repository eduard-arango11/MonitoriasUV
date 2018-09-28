from django.views.generic import *
from Facultades.models import Facultad
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

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

class ListarFacultades(ListView):
    model = Facultad
    template_name = "listar_facultades.html"

    def get_context_data(self, **kwargs):
        context = super(ListarFacultades, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_facultades'] = True
        context['listar_facultades']= True
        return context

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