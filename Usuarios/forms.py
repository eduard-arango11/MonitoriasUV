from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, forms
from Usuarios.models import *

class IniciarSesionForm(AuthenticationForm):	
	class Meta:
		model = Usuario
		username = forms.CharField(label="Usuario", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
		password = forms.CharField(label="Contraseña", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class Formulario_registrar_estudiante(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Estudiante
        fields = ('nombres','primer_apellido','segundo_apellido','email','password1', 'password2','codigo','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento','programa_academico')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
        }

class Formulario_modificar_estudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombres','primer_apellido','segundo_apellido','email','codigo','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento','programa_academico')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
        }

class Formulario_registrar_director(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Director
        fields = ('nombres','primer_apellido','segundo_apellido','email','password1', 'password2','tipo_documento','lugar_expedicion_documento','numero_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento','programa_academico')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
        }

class Formulario_modificar_director(forms.ModelForm):
    class Meta:
        model = Director
        fields = ('nombres','primer_apellido','segundo_apellido','email','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento','programa_academico')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
        }

class Formulario_registrar_operario(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Operario
        fields = ('nombres','primer_apellido','segundo_apellido','email','password1', 'password2','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento','cargo','dependencia')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
        }

class Formulario_modificar_operario(forms.ModelForm):
    class Meta:
        model = Operario
        fields = ('nombres','primer_apellido','segundo_apellido','email','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento','cargo','dependencia')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
        }

class Formulario_registrar_administrador(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Administrador
        fields = ('nombres','primer_apellido','segundo_apellido','email','password1', 'password2','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
        }

class Formulario_modificar_administrador(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ('nombres','primer_apellido','segundo_apellido','email','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
        }
