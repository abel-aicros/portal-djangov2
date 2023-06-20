
from django.urls import path
from Documentos.views import *

urlpatterns = [   
    path('', documentosView, name = 'documentos')  
]