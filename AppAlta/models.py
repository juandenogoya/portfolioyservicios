from django.db import models

from django.contrib.auth.models import User

# Create your models here.

#Modelo Contacto
class Contacto (models.Model):
    nombre = models.CharField (max_length=50)
    apellido = models.CharField (max_length=50)
    email = models.EmailField()
    telefono =  models.IntegerField()
    mensaje = models.CharField(max_length=2000)

    def __str__(self):
        return self.nombre, self.apellido, self.email


class Avatar (models.Model):
    imagen = models.ImageField (upload_to= "avatars")
    user = models.ForeignKey (User, on_delete= models.CASCADE)

class ImagenEquipo (models.Model):
    imagen = models.ImageField (upload_to= "equipo")
    user = models.ForeignKey (User, on_delete= models.CASCADE)


class EmpresaServicio (models.Model):
    razonSocial = models.CharField(max_length=50)
    cuit = models.IntegerField()
    email = models.EmailField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.razonSocial, self.cuit   


