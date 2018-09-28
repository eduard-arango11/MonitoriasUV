from django import forms
from .models import *

class Formulario_registrar_dependencia(forms.ModelForm):
	class Meta:
		model = Dependencia
		fields = ['nombre','estado']
