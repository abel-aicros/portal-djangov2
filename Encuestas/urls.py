from django.urls import path

from Encuestas.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', encuestasView, name = 'encuestas'),
    path('<int:id>', encuestaView, name = 'encuesta')   
]