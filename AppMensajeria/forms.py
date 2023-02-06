from django import forms
from .models import *
import datetime

class mensajesForm (forms.Form):
    titulo = forms.CharField (max_length=200)
    fecha = forms.DateField(label = "Fecha")
    nombre = forms.CharField (label= "Nombre", max_length=50)
    apellido = forms.CharField (label= "Apellido", max_length=50)
    email = forms.EmailField(label="Email")
    telefono =  forms.IntegerField(label = "Telefono")
    texto_msj = forms.CharField(label = "Mensaje", max_length=2000)

    class Meta:
        model = Mensajeria
        fields = ('titulo', 'fecha', 'nombre', 'apellido', 'email', 'telefono', 'texto_msj')
