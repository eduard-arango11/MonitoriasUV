from django import forms
from .models import *
from Usuarios.models import Estudiante

class Formulario_registrar_oferta(forms.ModelForm):
    class Meta:
        model = OfertaMonitoria
        fields = ['perfil_requerido', 'tipo_monitoria', 'sede', 'criterios_seleccion','periodo_duracion','horario_ejecucion','horas_semanales','plazo_solicitudes','fecha_seleccion','fecha_adjudicacion','estado']
        widgets = {
            'perfil_requerido' : forms.Textarea(),
            'plazo_solicitudes': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
            'fecha_seleccion': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
            'fecha_adjudicacion': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
        }

class Formulario_registrar_aplicacion(forms.ModelForm):
    class Meta:
        model = AplicacionOferta
        fields = ['estudiante', 'oferta', 'estado']

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
                'fecha_finalizacion_curso': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
            }

class Formulario_aprobar_d10(forms.ModelForm):
    class Meta:
        model = D10
        fields = ['promedio_acumulado','estado_aprobacion']