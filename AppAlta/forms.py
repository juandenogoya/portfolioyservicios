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



class UserEditForm (UserCreationForm):
    email = forms.EmailField(label= "Email")
    password1 = forms.CharField (label= "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField (label= "Confirmar Contraseña", widget= forms.PasswordInput)
    first_name = forms.CharField (label = "Modificar Nombre")
    last_name = forms.CharField (label= "Modificar Apellido")

    class Meta: 
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_text = {k:"" for k in fields}


class EmpresaFormulario (forms.Form):
    razonSocial = forms.CharField (label= "Razon Social", max_length=50)
    cuit = forms.IntegerField (label= "CUIT")
    email = forms.EmailField(label="Email")
    telefono =  forms.IntegerField(label = "Telefono")
    direccion = forms.CharField(label = "Domicilio", max_length=50)

