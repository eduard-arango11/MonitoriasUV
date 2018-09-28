from django.views.generic import *
from Dependencias.models import Dependencia
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class RegistrarDependencia(SuccessMessageMixin, CreateView):
    model = Dependencia
    form_class = Formulario_registrar_dependencia
    template_name = "registrar_dependencia.html"
    success_url = reverse_lazy('registrar_dependencia')
    success_message = "La dependencia fue registrada exitosamente"

    def form_valid (self, form):
        self.object = form.save()
        return super(RegistrarDependencia, self).form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super(RegistrarDependencia, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_dependencias'] = True
        context['registrar_dependencia']= True
        return context

class ListarDependencias(ListView):
    model = Dependencia
    template_name = "listar_dependencias.html"

    def get_context_data(self, **kwargs):
        context = super(ListarDependencias, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_dependencias'] = True
        context['listar_dependencias']= True
        return context

class EditarDependencia(SuccessMessageMixin, UpdateView):
    model = Dependencia
    form_class = Formulario_registrar_dependencia
    template_name = "registrar_dependencia.html"
    success_url = reverse_lazy('listar_dependencias')
    success_message = "La dependencia fue modificada exitosamente"
    
    def get_context_data(self, **kwargs):
        context = super(EditarDependencia, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_dependencias'] = True
        context['listar_dependencias']= True
        return context