from django import forms
from .models import *

class Formulario_registrar_facultad(forms.ModelForm):
	class Meta:
		model = Facultad
		fields = ['nombre', 'estado']
