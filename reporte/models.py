from django.db import models
from estudiante.models import Estudiante

# Create your models here.
class EstadoCuenta(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)
    fechaEmision = models.DateTimeField(auto_now_add=True)
    emisor = models.CharField(max_length=50)
    
    def __str__(self):
        return '%s %s' % (self.estudiante.nombre, self.fechaEmision)