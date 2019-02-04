from django import forms
from .models import *

class Formulario_registrar_oferta(forms.ModelForm):
    class Meta:
        model = OfertaMonitoria
        fields = ['descripcion_oferta','perfil_requerido', 'tipo_monitoria', 'sede', 'criterios_seleccion','periodo_duracion','horario_ejecucion','horas_semanales','plazo_solicitudes','fecha_seleccion','fecha_adjudicacion','estado']
        widgets = {
            'descripcion_oferta': forms.Textarea(attrs={'rows':3, 'cols':15}),
            'perfil_requerido' : forms.Textarea(attrs={'rows':4, 'cols':15}),
            'plazo_solicitudes': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'fecha_seleccion': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'fecha_adjudicacion': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
        }