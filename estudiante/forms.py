from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'numId', 'telefono', 'colegio', 'carnet', 'grado', 'curso']