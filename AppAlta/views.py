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

def prospectos (request):
    return render (request, "prospectos.html")

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

@login_required
def editarPerfil (request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm (request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info ["email"]
            usuario.password1 = info ["password1"]
            usuario.password2 = info ["password2"]
            usuario.first_name = info ["first_name"]
            usuario.last_name = info ["last_name"]
            usuario.save()
            return render (request, "inicio.html", {"mensaje": f"Usuario {usuario.username} Actualizado"})
        else:
            return render (request, "editarPerfil.html", {"form": form, "nombreusuario": usuario.username})

    else:
        form = UserEditForm (instance= usuario)
        return render (request, "editarPerfil.html", {"form": form, "nombreusuario": usuario.username}) 

@login_required
def prospectoForm (request):
    if request.method == "POST":
        form = EmpresaFormulario(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            empresa = informacion ["empresa"]
            cuit = informacion ["cuit"]
            email = informacion ["email"]
            telefono = informacion ["telefono"]
            direccion = informacion ["direccion"]
            prospecto = EmpresaServicio (empresa = empresa, cuit=cuit, email = email, telefono = telefono, direccion = direccion)
            prospecto.save()
            return render (request, "inicio.html", {"mensaje": "Prospecto Guardado"})
        else:
            return render (request, "prospectoForm.html", {"form": form, "mensaje": "Error al Cargar Empresa - Reintentar"})
    else:
        formulario = EmpresaFormulario()
        return render (request, "prospectoForm.html", {"form": formulario})

@login_required
def prospectoBuscar (request):
    return render (request, "prospectoBuscar.html")

@login_required
def buscar (request):
    empresa = request.GET ['empresa']
    if empresa!="":
        prospecto = EmpresaServicio.objects.filter(empresa__icontains= empresa)
        return render (request, "resultadoBuscar.html", {"prospecto": prospecto})
    else:
        return render (request, "prospectoBuscar.html", {"mensaje": "Ingresar Empresa"})

@login_required
def prospectoMostrar (request):
    prospecto = EmpresaServicio.objects.all()
    return render (request, "prospectos.html", {"prospecto": prospecto})


    