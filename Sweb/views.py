"""from django.http import HttpResponse"""
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from Productos.models import Producto_Aicros, Producto_Distribuido_Aicros

from Servicios.models import Servicio_Aicros
from .models import *
from django.conf import settings
from django.core import mail
# from django.core.mail import EmailMessage
from datetime import datetime
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
import os 
from django.contrib import messages

class Counter:
    count = 6

    def increment(self):
        self.count += 1
        return ''

    def decrement(self):
        self.count -= 1
        return ''

    def double(self):
        self.count *= 2
        return ''

        # {{ varint|add:"2" }}
        # {{ varint|add:"-1" }}

def noticiasView(request, id=1):
    noticia = Noticia.objects.all().filter(id=id)  
    print(noticia)
    banner_title = BannerTitle.objects.first()
    if noticia:
        if noticia[0].show ==True:
            noticia[0].Introducción_de_Noticia_parsed = noticia[0].Introducción_de_Noticia.replace("#", "%23")
            return render(request, 'noticia.html',{'noticia':noticia,'banner_title': banner_title,})
        else:
            pass
            # return render(request, '403.html')
    else :
        pass
        
def home(request):
   return render(request, 'documento.html', {'range': range(1,6),
                                             'PaginaActual'  : "'noticias'",})


def primeraVista(request):
    try:    
        if request.method == 'POST':
            name = request.POST['Nombre']
            category = request.POST['Personalidad']
            email = request.POST['Correo']
            message = request.POST['Contenido']
            try:
                with mail.get_connection() as connection:
                    mail.EmailMessage(
                    'Mensaje de portal Aicros',
                    f"{name}: ({email}), {category}{os.linesep}{message}",
                    settings.EMAIL_HOST_USER,
                    settings.EMAIL_RECEIVER,
                    connection=connection,
                    ).send()
                messages.success(request, 'Mensaje enviado!')
            except Exception as e:
                messages.error(request, 'Error al enviar mensaje')
                print(e)    
        

        template_name = "index.html"

        carrusel = Carrusel.objects.all()
        inicioprod = InicioProducto.objects.all()
        carrusel_productos = Producto_Aicros.objects.all().union(Producto_Distribuido_Aicros.objects.all(), all=True)
        inicioServicio = InicioServicio.objects.all()
        carrusel_servicios = Servicio_Aicros.objects.all()
        lineaNegocio = Líneas_de_Negocio.objects.all()
        cifra = Cifra.objects.all()
        alianza = Alianza.objects.all()
        noticias = Noticia.objects.all().filter(show=True)
        for n in noticias:
            n.Introducción_de_Noticia_parsed = n.Introducción_de_Noticia.replace("#", "%23")
        
        promo_title = PromotionsTitle.objects.all()
        # products_title = PromotionsTitle.objects.all()
        # services_title = ServicesTitle.objects.all()
        buss_lines_title = BussinesLinesTitle.objects.all()
        stats_title = StatsTitle.objects.all()
        news_title = NewsTitle.objects.all()
        alliance_title = AllianceTitle.objects.all()
        banner_title = BannerTitle.objects.first()
        
        context = {

            'Carrusel': carrusel,
            'InicioProducto': inicioprod,
            'Carrusel_Productos': carrusel_productos,
            'InicioServicio': inicioServicio,
            'Carrusel_Servicios': carrusel_servicios,
            'Líneas_de_Negocio': lineaNegocio,
            'Cifra': cifra,
            'noticias': noticias,
            'Alianza': alianza,
            
            'promo_title': promo_title,
            'buss_lines_title': buss_lines_title,
            'stats_title': stats_title,
            'news_title': news_title,
            'alliance_title': alliance_title,
            
            'PaginaActual'  : "'Home'",
            'banner_title': banner_title,
            }

        return render(request, template_name, context)
    except Exception as e:
        print(e)
        return e

def err404_view(request, exception):
    try:
        banner_title = BannerTitle.objects.first()
        page404 = Page404.objects.all()
        context = {'banner_title': banner_title,
                'p404': page404,
                'PaginaActual': "'404'"}
        return render(request, '404.html', context, status=404)
    except Exception as e:
        print(e)
        return e
