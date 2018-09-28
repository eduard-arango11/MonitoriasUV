from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from monitorias.utilities import *

class RegistrarEstudiante(SuccessMessageMixin, CreateView):
	model = Estudiante
	form_class = Formulario_registrar_estudiante
	template_name = "registrar_estudiante.html" #Se puede crear un template para todos los crear haciendo uso de context??
	success_url = reverse_lazy('registrar_estudiante')
	success_message = "El estudiante fue registrado exitosamente"

	def form_valid (self, form):
		estudiante = form.instance
		estudiante.username = estudiante.email
		estudiante.rol = "Estudiante"
		self.object = form.save()
		return super(RegistrarEstudiante, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(RegistrarEstudiante, self).get_context_data(**kwargs)
		context['gestion_usuarios']= True
		context['gestion_estudiantes'] = True
		context['registrar_estudiante']= True
		context['creacion']=True
		return context
	
	@method_decorator(login_required)
	@method_decorator(verificar_rol(roles_permitidos=['Director','Administrador']))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class ListarEstudiantes (ListView):
	model = Estudiante
	template_name = "listar_estudiantes.html"
	
	def get_context_data(self, **kwargs):
		context = super(ListarEstudiantes, self).get_context_data(**kwargs)
		context['gestion_usuarios']= True
		context['gestion_estudiantes'] = True
		context['listar_estudiantes']= True
		return context

	@method_decorator(login_required)
	@method_decorator(verificar_rol(roles_permitidos=['Director','Administrador']))
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
		context['gestion_usuarios']= True
		context['gestion_estudiantes'] = True
		context['listar_estudiantes']= True
		return context

class RegistrarDirector(SuccessMessageMixin, CreateView):
	model = Director
	form_class = Formulario_registrar_director
	template_name = "registrar_director.html" #Se puede crear un template para todos los crear haciendo uso de context??
	success_url = reverse_lazy('registrar_director')
	success_message = "El director de programa fue registrado exitosamente"

	def form_valid (self, form):
		director = form.instance
		director.username = director.email
		director.rol = "Director"
		self.object = form.save()
		return super(RegistrarDirector, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(RegistrarDirector, self).get_context_data(**kwargs)
		context['gestion_usuarios']= True
		context['gestion_directores'] = True
		context['registrar_director']= True
		context['creacion']=True
		return context
	
	@method_decorator(login_required)
	@method_decorator(verificar_rol(roles_permitidos=['Administrador']))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class ListarDirectores (ListView):
	model = Director
	template_name = "listar_directores.html"
	
	def get_context_data(self, **kwargs):
		context = super(ListarDirectores, self).get_context_data(**kwargs)
		context['gestion_usuarios']= True
		context['gestion_directores'] = True
		context['listar_directores']= True
		return context
	
	@method_decorator(login_required)
	@method_decorator(verificar_rol(roles_permitidos=['Administrador','Director', 'Operario', 'Estudiante']))
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
		context['gestion_usuarios']= True
		context['gestion_directores'] = True
		context['listar_directores']= True
		return context

class RegistrarOperario(SuccessMessageMixin, CreateView):
	model = Operario
	form_class = Formulario_registrar_operario
	template_name = "registrar_operario.html" #Se puede crear un template para todos los crear haciendo uso de context??
	success_url = reverse_lazy('registrar_operario')
	success_message = "El operario fue registrado exitosamente"

	def form_valid (self, form):
		operario = form.instance
		operario.username = operario.email
		operario.rol = "Operario"
		self.object = form.save()
		return super(RegistrarOperario, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(RegistrarOperario, self).get_context_data(**kwargs)
		context['gestion_usuarios']= True
		context['gestion_operarios'] = True
		context['registrar_operario']= True
		context['creacion']=True
		return context
	
	@method_decorator(login_required)
	@method_decorator(verificar_rol(roles_permitidos=['Administrador']))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class ListarOperarios (ListView):
	model = Operario
	template_name = "listar_operarios.html"
	
	def get_context_data(self, **kwargs):
		context = super(ListarOperarios, self).get_context_data(**kwargs)
		context['gestion_usuarios']= True
		context['gestion_operarios'] = True
		context['listar_operarios']= True
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
		context['gestion_usuarios']= True
		context['gestion_operarios'] = True
		context['listar_operarios']= True
		return context

class RegistrarAdministrador(SuccessMessageMixin, CreateView):
	model = Administrador
	form_class = Formulario_registrar_administrador
	template_name = "registrar_administrador.html" #Se puede crear un template para todos los crear haciendo uso de context??
	success_url = reverse_lazy('registrar_administrador')
	success_message = "El administrador fue registrado exitosamente"

	def form_valid (self, form):
		administrador = form.instance
		administrador.username = administrador.email
		administrador.rol = "Administrador"
		self.object = form.save()
		return super(RegistrarAdministrador, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(RegistrarAdministrador, self).get_context_data(**kwargs)
		context['gestion_usuarios']= True
		context['gestion_administradores'] = True
		context['registrar_administrador']= True
		context['creacion']=True
		return context
	
	@method_decorator(login_required)
	@method_decorator(verificar_rol(roles_permitidos=['Administrador']))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class ListarAdministradores (ListView):
	model = Administrador
	template_name = "listar_administradores.html"
	
	def get_context_data(self, **kwargs):
		context = super(ListarAdministradores, self).get_context_data(**kwargs)
		context['gestion_usuarios']= True
		context['gestion_administradores'] = True
		context['listar_administradores']= True
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
		context['gestion_usuarios']= True
		context['gestion_administradores'] = True
		context['listar_administradores']= True
		return context