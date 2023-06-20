from django.shortcuts import render
from django.views import View
from .models import *
from Sweb.models import BannerTitle, Líneas_de_Negocio
# Create your views here.



def serviciosView(request):
    banner_title = BannerTitle.objects.first()
    template_name = "Servicios/servicios.html"
    encabezado_servicio = Encabezado_Servicio.objects.all()
    descripcion_servicios_aicros = Descripcion_Servicios_Aicros.objects.all()
    servicio_aicros = Servicio_Aicros.objects.all()
    lineas_de_negocio = Líneas_de_Negocio.objects.all()
    servicio_aicros_dict = {}
    
    for servicio in list(servicio_aicros):
        if(servicio.line_id in servicio_aicros_dict.keys()):
            servicio_aicros_dict[servicio.line_id].append(servicio)
        else:
            servicio_aicros_dict[servicio.line_id] = [servicio]
    
    context = {
        
    'Encabezado_Servicio': encabezado_servicio,
    'Descripcion_Servicios_Aicros': descripcion_servicios_aicros,
    'Servicio_Aicros_Dict': servicio_aicros_dict,
    'PaginaActual'  : "'Servicios'",
    'lineas_de_negocio': lineas_de_negocio,
    'servicio_aicros':servicio_aicros,
    'banner_title': banner_title,
    
    }

    return render(request, template_name, context)
   