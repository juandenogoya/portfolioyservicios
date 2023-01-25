from django.shortcuts import render
from .models import *

from AppAlta.forms import *
from django.urls import reverse_lazy


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio (request):
    return render (request, "inicio.html")

def nosotros (request):
    return render (request, "nosotros.html")

def portfolio (request):
    return render (request, "portfolio.html")

def equipo (request):
    return render (request, "equipo.html")

def contactoForm (request):
    if request.method == "POST":
        form = ContactoFormulario(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion ["nombre"]
            apellido = informacion ["apellido"]
            email = informacion ["email"]
            telefono = informacion ["telefono"]
            mensaje = informacion ["mensaje"]
            contacto = Contacto (nombre = nombre, apellido=apellido, email = email, telefono = telefono, mensaje = mensaje)
            contacto.save()
            return render (request, "inicio.html", {"mensaje": "Mensaje Enviado"})
        else:
            return render (request, "contactoForm.html", {"form": form, "mensaje": "Error al Cargar Mensaje - Reintentar"})
    else:
        formulario = ContactoFormulario()
        return render (request, "contactoForm.html", {"form": formulario})

def register (request):
    if request.method == "POST":
        form = RegistroUsuarioForm (request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render (request, "inicio.html", {"mensaje": f"Usuario {username} creado"})
        else:
            return render (request, "register.html",{"form": form, "mensaje": "Error al Crear Usuario"})

    else: 
        form = RegistroUsuarioForm()
        return render (request, "register.html", {"form": form})
    

def login_usuario (request):
    if request.method == "POST":
        form= AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usu = info ["username"]
            clave = info ["password"]
            usuario = authenticate (username = usu, password = clave) #Verifica si el usuario existe, lo devuelve sino, devuelve NONE.
            if usuario is not None:
                login(request, usuario)
                return render (request, "inicio.html", {"mensaje": f"Usuario {usu} - Ingreso Correcto"})
            else: 
                return render (request, "login.html", {"form": form, "mensaje": "Usuario o Contraseña Incorrecto"})
        else: 
           return render (request, "login.html", {"form": form, "mensaje": "Usuario o Contraseña Incorrecto"}) 
    else: 
        form = AuthenticationForm()
        return render (request, "login.html", {"form": form})

