from django import forms
from .models import Cuenta
from estudiante.models import Estudiante
from pago.models import Pago

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['estudiante', 'saldo', 'estado', 'pagos']
    
    # Si deseas añadir un widget para los pagos, puedes hacerlo aquí
    # Si los pagos son muchos, puedes utilizar un widget de selección múltiple
    pagos = forms.ModelMultipleChoiceField(queryset=Pago.objects.all(), required=False)
