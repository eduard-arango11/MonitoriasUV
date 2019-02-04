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
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'codigo': forms.NumberInput(),
            'telefono': forms.NumberInput(),
            'numero_documento': forms.NumberInput(),
        }

class Formulario_modificar_estudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombres','primer_apellido','segundo_apellido','email','codigo','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento','programa_academico')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'codigo': forms.NumberInput(),
            'telefono': forms.NumberInput(),
            'numero_documento': forms.NumberInput(),
        }

class Formulario_registrar_director(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Director
        fields = ('nombres','primer_apellido','segundo_apellido','email','password1', 'password2','tipo_documento','lugar_expedicion_documento','numero_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento','programa_academico')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'telefono': forms.NumberInput(),
            'numero_documento': forms.NumberInput(),
        }

class Formulario_modificar_director(forms.ModelForm):
    class Meta:
        model = Director
        fields = ('nombres','primer_apellido','segundo_apellido','email','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento','programa_academico')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'telefono': forms.NumberInput(),
            'numero_documento': forms.NumberInput(),
        }

class Formulario_registrar_operario(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Operario
        fields = ('nombres','primer_apellido','segundo_apellido','email','password1', 'password2','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento','cargo','dependencia')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'telefono': forms.NumberInput(),
            'numero_documento': forms.NumberInput(),
        }

class Formulario_modificar_operario(forms.ModelForm):
    class Meta:
        model = Operario
        fields = ('nombres','primer_apellido','segundo_apellido','email','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento','cargo','dependencia')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'telefono': forms.NumberInput(),
            'numero_documento': forms.NumberInput(),
        }

class Formulario_registrar_administrador(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Administrador
        fields = ('nombres','primer_apellido','segundo_apellido','email','password1', 'password2','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'telefono': forms.NumberInput(),
            'numero_documento': forms.NumberInput(),
        }

class Formulario_modificar_administrador(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ('nombres','primer_apellido','segundo_apellido','email','tipo_documento','numero_documento','lugar_expedicion_documento','telefono','genero','lugar_nacimiento','fecha_nacimiento')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'telefono': forms.NumberInput(),
            'numero_documento': forms.NumberInput(),
        }


class Formulario_registrar_d10_datos_basicos(forms.ModelForm):
    class Meta:
        model = DatosBasicosD10
        fields = '__all__'

        widgets = {
            'perfil_ocupacional': forms.Textarea(),
            'sistemas_que_maneja': forms.Textarea(),
        }


class Formulario_registrar_d10_datos_educacion(forms.ModelForm):
    class Meta:
        model = DatosEducacionD10
        fields = '__all__'


class Formulario_registrar_d10_datos_capacitacion(forms.ModelForm):
    class Meta:
        model = DatosCapacitacionD10
        fields = '__all__'

        widgets = {
            'fecha_finalizacion_curso': forms.DateInput(attrs={'class': 'datepicker', 'autocomplete': 'off'}),
        }


class Formulario_registrar_d10_datos_experiencia_laboral(forms.ModelForm):
    class Meta:
        model = DatosExperienciaLaboralD10
        fields = '__all__'

        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'datepicker', 'autocomplete': 'off'}),
            'fecha_finalizacion': forms.DateInput(attrs={'class': 'datepicker', 'autocomplete': 'off'}),
            'funciones_realizadas': forms.Textarea(),
            'logros': forms.Textarea(),
        }


class Formulario_registrar_d10_datos_horario_disponible(forms.ModelForm):
    class Meta:
        model = DatosHorarioDisponibleD10
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(Formulario_registrar_d10_datos_horario_disponible, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'clockpicker'
            self.fields[field].widget.attrs['placeholder'] = ' '


class Formulario_aprobar_d10(forms.ModelForm):
    class Meta:
        model = D10
        fields = ['promedio_acumulado', 'estado_aprobacion']