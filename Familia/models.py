from django.db import models

# Create your models here.
class Integrantes(models.Model):
    nombre =  models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    fechaNacimiento = models.DateField()
    dni = models.IntegerField()
    