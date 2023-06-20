
from django.urls import path
from Servicios.views import *

urlpatterns = [
    path('', serviciosView, name = 'servicios')  
]