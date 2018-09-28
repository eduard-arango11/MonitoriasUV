from django.views.generic import *
from ProgramasAcademicos.models import ProgramaAcademico
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class RegistrarPrograma(SuccessMessageMixin, CreateView):
    model = ProgramaAcademico
    form_class = Formulario_registrar_programa
    template_name = "registrar_programa.html"
    success_url = reverse_lazy('registrar_programa')
    success_message = "El programa academico fue registrado exitosamente"

    def form_valid (self, form):
        self.object = form.save()
        return super(RegistrarPrograma, self).form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super(RegistrarPrograma, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_programas'] = True
        context['registrar_programa']= True
        return context

class ListarProgramas(ListView):
    model = ProgramaAcademico
    template_name = "listar_programas.html"

    def get_context_data(self, **kwargs):
        context = super(ListarProgramas, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_programas'] = True
        context['listar_programas']= True
        return context

class EditarPrograma(SuccessMessageMixin, UpdateView):
    model = ProgramaAcademico
    form_class = Formulario_registrar_programa
    template_name = "registrar_programa.html"
    success_url = reverse_lazy('listar_programas')
    success_message = "El programa academico fue modificado exitosamente"
    
    def get_context_data(self, **kwargs):
        context = super(EditarPrograma, self).get_context_data(**kwargs)
        context['gestion_universidad']= True
        context['gestion_programas'] = True
        context['listar_programas']= True
        return context