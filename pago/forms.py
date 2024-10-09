from django import forms
from .models import Pago

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['valor', 'causacion', 'fechaLimite', 'estado', 'mes']
