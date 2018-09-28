from django import forms
from .models import *

class Formulario_registrar_programa(forms.ModelForm):
	class Meta:
		model = ProgramaAcademico
		fields = ['nombre_programa', 'codigo_programa', 'jornada', 'facultad']
