from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('inicio/', inicio, name = 'inicio'),
    path ('nosotros/', nosotros, name = 'nosotros'),
    path ('prospectos/', prospectos, name = 'prospectos'),
    path ('equipo/', equipo, name = 'equipo'),
    path ('contactoForm/', contactoForm, name = 'contactoForm'),

    path ('register/', register, name = 'register'),
    path ('login/', login_usuario, name = 'login'),
    path ('logout/', LogoutView.as_view(), name='logout'),

    path ('editarPerfil/', editarPerfil, name = 'editarPerfil'),


    path ('prospectoForm/', prospectoForm, name = 'prospectoForm'),
    path ('prospectoMostrar/', prospectoMostrar, name= 'prospectoMostrar'),
    path ('prospectoBuscar/', prospectoBuscar, name = 'prospectoBuscar'),
    path ('buscar/', buscar, name = 'buscar'),

]
