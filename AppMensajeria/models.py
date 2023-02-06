from django.db import models
import datetime

# Create your models here.

class Mensajeria (models.Model):
    titulo = models.CharField (max_length= 100)
    fecha = models.DateField()
    nombre = models.CharField (max_length=50)
    apellido = models.CharField (max_length=50)
    email = models.EmailField()
    telefono =  models.IntegerField()
    texto_msj = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.titulo} - {self.nombre} - {self.apellido} - {self.fecha}"


