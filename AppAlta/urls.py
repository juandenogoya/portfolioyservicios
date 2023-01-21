from django.urls import path
from .views import *

urlpatterns = [
    path ('inicio/', inicio, name = 'inicio'),
    path ('nosotros/', nosotros, name = 'nosotros'),
    


]