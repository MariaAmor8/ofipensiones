from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, default=None)
    numId = models.IntegerField(default=None)
    telefono = models.IntegerField(default=None)
    colegio = models.CharField(max_length=100, default=None)
    carnet = models.CharField(max_length=50, default=None)
    grado = models.CharField(max_length=100, default=None)
    curso = models.CharField(max_length=100, default=None)
    emailPadreFamilia = models.CharField(max_length=100, default=None)
    
    def __str__(self):
        return '{}'.format(self.nombre)