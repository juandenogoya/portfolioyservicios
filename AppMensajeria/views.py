from django.shortcuts import render
from .forms import *

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def mensajes (request):
    if request.method == "POST":
        form = mensajesForm (request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            titulo = informacion ['titulo']
            fecha = informacion ['fecha']
            nombre = informacion ['nombre']
            apellido = informacion ['apellido']
            email = informacion ['email']
            telefono = informacion ['telefono']
            texto_msj = informacion ['texto_msj']
            mensaje = Mensajeria (titulo=titulo, fecha=fecha, nombre=nombre, apellido=apellido, email=email, telefono=telefono, texto_msj=texto_msj)
            mensaje.save()
            return render (request, "inicio.html", {"mensaje": 'Mensaje Enviado'})
        else:
            return render (request, "inicio.html", {"mensaje" : "Error al enviar Mensajes"})
    else: 
        form = mensajesForm () 
        return render (request, "mensajes.html", {"form": form})

@login_required
def verMensajes (request):
    titulo = Mensajeria.objects.all()
    return render (request, 'verMensajes.html', {'titulo': titulo})

