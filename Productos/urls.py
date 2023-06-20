
from django.urls import path
from Productos.views import *

urlpatterns = [
    path('', productosView, name = 'productos')   
]