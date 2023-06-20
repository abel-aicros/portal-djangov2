from django.contrib import admin
from .models import *

# --------------------Encabezado Documentos--------------------
admin.site.register(Encabezado_Documentos)

# --------------------Texto Documentos Rápidos--------------------
admin.site.register(Texto_Documentos_Rapidos)

# --------------------Documentos de Rápido Acceso--------------------
admin.site.register(Seccion)
admin.site.register(Documento)
admin.site.register(DocumentoRap)