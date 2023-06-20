from django.contrib import admin
from Encuestas.models import *
# Register your models here.
admin.site.register(Respuesta)
admin.site.register(Pregunta)
admin.site.register(Encuesta)
admin.site.register(GrupoDeRespuestas)
admin.site.register(SurveyTitle)
