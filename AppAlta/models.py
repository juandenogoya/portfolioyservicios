from django.db import models

# Create your models here.

#Modelo Contacto
class Contacto (models.Model):
    nombre = models.CharField (max_length=50)
    apellido = models.CharField (max_length=50)
    email = models.EmailField()
    telefono =  models.IntegerField()
    mensaje = models.CharField(max_length=2000)

