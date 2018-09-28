from django import forms
from .models import *

class Formulario_registrar_unidad(forms.ModelForm):
	class Meta:
		model = Unidad
		fields = ['nombre','estado','facultad']
