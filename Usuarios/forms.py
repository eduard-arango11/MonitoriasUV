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

    def __init__(self, *args, **kwargs):
        super(Formulario_registrar_d10_datos_basicos, self).__init__(*args, **kwargs)
        self.fields['estado_civil'].widget.attrs = {'class': 'form-control required'}
        self.fields['numero_de_personas_a_cargo'].widget.attrs = {'class': 'form-control required'}
        self.fields['posicion_familiar'].widget.attrs = {'class': 'form-control required'}
        self.fields['direccion_residencia'].widget.attrs = {'class': 'form-control required'}
        self.fields['estrato'].widget.attrs = {'class': 'form-control required'}
        self.fields['perfil_ocupacional'].widget.attrs = {'rows': '5','class': 'form-control required'}
        self.fields['barrio'].widget.attrs = {'class': 'form-control required'}
        self.fields['ciudad'].widget.attrs = {'class': 'form-control required'}
        self.fields['departamento'].widget.attrs = {'class': 'form-control required'}
        self.fields['nombre_acudiente'].widget.attrs = {'class': 'form-control required'}
        self.fields['telefono_acudiente'].widget.attrs = {'class': 'form-control required'}
        self.fields['sistemas_que_maneja'].widget.attrs = {'rows': '5', 'class': 'form-control required'}

    class Meta:
        model = DatosBasicosD10
        fields = '__all__'

        widgets = {
            'perfil_ocupacional': forms.Textarea(attrs={'rows': '10'}),
            'sistemas_que_maneja': forms.Textarea(attrs={'rows': '10'}),
            'semestre': forms.DateTimeInput(attrs={'class': 'form-control required'})
        }


class Formulario_registrar_d10_datos_educacion(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Formulario_registrar_d10_datos_educacion, self).__init__(*args, **kwargs)
        self.fields['titulo_obtenido_bachillerato'].widget.attrs = {'class': 'form-control required'}
        self.fields['ano_finalizacion_bachillerato'].widget.attrs = {'class': 'form-control required'}
        self.fields['nombre_colegio_bachillerato'].widget.attrs = {'class': 'form-control required'}
        self.fields['ciudad_colegio_bachillerato'].widget.attrs = {'class': 'form-control required'}
        self.fields['plan_otros_estudios'].widget.attrs = {'class': 'form-control'}
        self.fields['semestres_otros_estudios'].widget.attrs = {'rows': '5','class': 'form-control'}
        self.fields['ano_finalizacion_otros_estudios'].widget.attrs = {'class': 'form-control'}
        self.fields['nombre_establecimiento_otros_estudios'].widget.attrs = {'class': 'form-control'}
        self.fields['ciudad_establecimiento_otros_estudios'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = DatosEducacionD10
        fields = '__all__'


class Formulario_registrar_d10_datos_capacitacion(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Formulario_registrar_d10_datos_capacitacion, self).__init__(*args, **kwargs)
        self.fields['nombre_establecimiento'].widget.attrs = {'class': 'form-control'}
        self.fields['nombre_curso'].widget.attrs = {'class': 'form-control'}
        self.fields['duracion_cruso'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = DatosCapacitacionD10
        fields = '__all__'

        widgets = {
            'fecha_finalizacion_curso': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
        }


class Formulario_registrar_d10_datos_experiencia_laboral(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Formulario_registrar_d10_datos_experiencia_laboral, self).__init__(*args, **kwargs)
        self.fields['nombre_empresa'].widget.attrs = {'class': 'form-control'}
        self.fields['cargo'].widget.attrs = {'class': 'form-control'}
        self.fields['funciones_realizadas'].widget.attrs = {'rows': '5', 'class': 'form-control'}
        self.fields['logros'].widget.attrs = {'rows': '5', 'class': 'form-control'}
        self.fields['jefe_inmediato'].widget.attrs = {'class': 'form-control'}
        self.fields['cargo_jefe'].widget.attrs = {'class': 'form-control'}
        self.fields['telefono_empresa'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = DatosExperienciaLaboralD10
        fields = '__all__'

        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
            'fecha_finalizacion': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
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
            self.fields[field].widget.attrs['class'] = 'clockpicker color_blanco'
            self.fields[field].widget.attrs['placeholder'] = ' '
            self.fields[field].widget.attrs['readonly'] = 'true'


class Formulario_aprobar_d10(forms.ModelForm):
    class Meta:
        model = D10
        fields = ['promedio_acumulado', 'estado_aprobacion']