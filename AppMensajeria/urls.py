from django.urls import path
from .views import *

urlpatterns = [
    path ('mensajes/', mensajes, name = 'mensajes'),
    path ('verMensajes/', verMensajes, name = 'verMensajes'),

    path ('borrarMensaje/<id>', borrarMensaje, name = 'borrarMensaje'),



]