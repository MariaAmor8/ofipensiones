from django.db import models
from estudiante.models import Estudiante
# Create your models here.

class Pago(models.Model):
    valor = models.IntegerField(default=None)
    causacion = models.CharField(max_length=80)
    fechaLimite = models.DateField()
    
    ESTADO_PAGO = [ ('PAG', 'Pagado'),('NOP', 'No Pagado'),]
   
    estado = models.CharField(
        max_length=3, 
        choices=ESTADO_PAGO,
        default='NOP',
    )
    
    MESES = [
        ('01', 'Enero'),
        ('02', 'Febrero'),
        ('03', 'Marzo'),
        ('04', 'Abril'),
        ('05', 'Mayo'),
        ('06', 'Junio'),
        ('07', 'Julio'),
        ('08', 'Agosto'),
        ('09', 'Septiembre'),
        ('10', 'Octubre'),
        ('11', 'Noviembre'),
        ('12', 'Diciembre'),
    ]
    
    mes = models.CharField(
        max_length=2,  # Porque almacenamos los valores como '01', '02', etc.
        choices=MESES,
        default='01',  # Opción predeterminada (por ejemplo, 'Enero')
    )
    
    def __str__(self):
        return self.causacion+" - "+ str(self.valor)