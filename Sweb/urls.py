
from django.urls import path

from Sweb.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', primeraVista, name = 'inicio'),
    # path('', primeraVista2, name = 'inicio'),
    # path('encuesta/', encuestaView, name = 'encuesta'),
    path('noticias/<int:id>', noticiasView, name = 'noticias')
   # path('contact/', contactView, name = 'contactar'), 
   # path('courses/', coursesView, name = 'cursos')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'Sweb.views.err404_view'