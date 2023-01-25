from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactoFormulario (forms.Form):
    nombre = forms.CharField (label= "Nombre", max_length=50)
    apellido = forms.CharField (label= "Apellido", max_length=50)
    email = forms.EmailField(label="Email")
    telefono =  forms.IntegerField(label = "Telefono")
    mensaje = forms.CharField(label = "Mensaje", max_length=2000)


class RegistroUsuarioForm (UserCreationForm):
    username = forms.CharField (label= "Usuario", max_length=50)
    email = forms.EmailField(label= "Email")
    password1 = forms.CharField (label= "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField (label= "Confirmar Contraseña", widget= forms.PasswordInput)


    class Meta: #Una clase para configurar el Usuario, configurar el Formulario de registro de usuario.
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k:"" for k in fields} #linea que borra las ayuda del formulario de crear usuario.


