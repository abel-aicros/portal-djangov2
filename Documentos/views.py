from django.shortcuts import render
from django.views import View

from Sweb.models import BannerTitle
from .models import *
# Create your views here.


from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.text import normalize_newlines


    

def documentosView(request):
    template_name = "Documentos/documento.html"
    banner_title = BannerTitle.objects.first()
    try:
        filtro = request.GET['filtrado']
    except:
        filtro =''
    
    secciones = Seccion.objects.all()
    documentos = Documento.objects.filter(nombre__icontains = filtro)

    encabezado_documentos = Encabezado_Documentos.objects.all()

    texto_documentos_rapidos = Texto_Documentos_Rapidos.objects.all()

    doc_rap = DocumentoRap.objects.all()
    data = []
    docs_by_section={}
    for i in list(secciones):
        docs_by_section[i]=[]
        for j in list(documentos):
            if i in j.seccion.all():
                docs_by_section[i].append(j)
        data.append(len(docs_by_section[i]))
        print(docs_by_section)
        print(data)







    context = {

    'Encabezado_Documentos': encabezado_documentos,
    'Texto_Documentos_Rapidos': texto_documentos_rapidos,
    'secciones': secciones,
    'documentos': documentos,
    'doc_rap': doc_rap,
    'PaginaActual'  : "'Documentos'",
    'filtro'        : filtro    ,
    'data' : data,
    'columnajs': 0,
    'docs_by_section': docs_by_section,
    'banner_title': banner_title,
    'vacio': len(docs_by_section.keys()),
     }
    
   
                        
        
    return render(request, template_name, context)
