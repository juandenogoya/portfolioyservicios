from django.shortcuts import render

# Create your views here.

def inicio (request):
    return render (request, "inicio.html")

def nosotros (request):
    return render (request, "nosotros.html")

def portfolio (request):
    return render (request, "portfolio.html")

