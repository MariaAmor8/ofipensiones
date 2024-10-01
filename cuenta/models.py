from django.db import models
from estudiante.models import Estudiante
from pago.models import Pago
# Create your models here.

class Cuenta(models.Model):
    
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)
    saldo = models.IntegerField(default=None)
    ESTADO_CUENTA = [
        ('MOR', 'Moroso'),
        ('NOM', 'No Moroso'),
    ]
    
    estado = models.CharField(
        max_length=3, 
        choices=ESTADO_CUENTA,
        default='NOM'
    )
    
    pagos = models.ManyToManyField(Pago, related_name='pagos')