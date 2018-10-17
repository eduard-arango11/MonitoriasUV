from django import forms
from .models import *

class Formulario_registrar_oferta(forms.ModelForm):
    class Meta:
        model = OfertaMonitoria
        fields = ['perfil_requerido', 'tipo_monitoria', 'sede', 'criterios_seleccion','periodo_duracion','horario_ejecucion','horas_semanales','plazo_solicitudes','fecha_seleccion','fecha_adjudicacion','estado']
        widgets = {
            'perfil_requerido' : forms.Textarea(),
            'plazo_solicitudes': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
            'fecha_seleccion': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
            'fecha_adjudicacion': forms.DateInput(attrs={'class':'datepicker', 'autocomplete': 'off'}),
            # 'criterios_seleccion': forms.DateInput(attrs={'class': 'chosen-select', 'multiple data-placeholder':'holaa'}),
        }

class Formulario_registrar_aplicacion(forms.ModelForm):
    class Meta:
        model = AplicacionOferta
        fields = ['estudiante', 'oferta', 'estado']

