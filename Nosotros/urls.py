
from django.urls import path
from Nosotros.views import *

urlpatterns = [   
    path('', aboutView, name = 'quienesSomos')    
]