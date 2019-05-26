from django import forms
from .models import *

class Formulario_registrar_oferta(forms.ModelForm):
    class Meta:
        model = OfertaMonitoria
        fields = ['descripcion_oferta','perfil_requerido', 'tipo_monitoria', 'sede', 'criterios_seleccion','periodo_duracion','horario_ejecucion','horas_semanales','plazo_solicitudes','fecha_seleccion','fecha_adjudicacion']
        widgets = {
            'descripcion_oferta': forms.Textarea(attrs={'rows':3, 'cols':15}),
            'perfil_requerido' : forms.Textarea(attrs={'rows':4, 'cols':15}),
            'plazo_solicitudes': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'fecha_seleccion': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
            'fecha_adjudicacion': forms.DateInput(attrs={'class':'datepicker color_blanco', 'autocomplete': 'off', 'readonly': 'true'}),
        }

    def clean(self):

        cleaned_data = super(Formulario_registrar_oferta, self).clean()
        plazo_solicitudes = cleaned_data.get("plazo_solicitudes")
        fecha_seleccion = cleaned_data.get("fecha_seleccion")
        fecha_adjudicacion = cleaned_data.get("fecha_adjudicacion")

        try:
            if plazo_solicitudes < fecha_seleccion and fecha_seleccion < fecha_adjudicacion:
                pass
            elif not plazo_solicitudes < fecha_seleccion:
                self._errors['fecha_seleccion'] = [
                    'La fecha de seleccion debe ser posterior al plazo para solicitudes']
            elif not fecha_seleccion < fecha_adjudicacion:
                self._errors['fecha_adjudicacion'] = [
                    'La fecha de adjudicacion debe ser posterior a la fecha de seleccion']
        except:
            pass