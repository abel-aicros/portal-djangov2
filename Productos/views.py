from django.shortcuts import render
from django.views import View

from Sweb.models import BannerTitle
from .models import *

# Create your views here.


def productosView(request):
    banner_title = BannerTitle.objects.first()
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = Producto_Aicros.objects.get(id=product_id) if request.POST['ptype'] == 'aicros' else Producto_Distribuido_Aicros.objects.get(id=product_id)
        product_name = product.título
        product_description  = product.descripción
        product_image = product.foto.url
        product_icon = product.ícono.url
        
        return render(request, 'Productos/producto.html', {'product_name': product_name, 'product_description':product_description, 'product_image': product_image, 'product_icon': product_icon,'banner_title': banner_title,})
    
    template_name = "Productos/productos.html"
    encabezado_producto = Encabezado_Producto.objects.all()
    descripcion_productos_aicros = Descripcion_Productos_Aicros.objects.all()
    descripcion_productos_distribuidos = Descripcion_Productos_Distribuidos.objects.all()
    producto_aicros = Producto_Aicros.objects.all()
    producto_distribuido_aicros = Producto_Distribuido_Aicros.objects.all()
    
    
    
    context = {
        
    'Encabezado_Producto': encabezado_producto,
    'Descripcion_Productos_Aicros': descripcion_productos_aicros,
    'Descripcion_Productos_Distribuidos': descripcion_productos_distribuidos,
    'Producto_Aicros': producto_aicros,
    'Producto_Distribuido_Aicros': producto_distribuido_aicros,
    'PaginaActual'  : "'Productos'", 
    'banner_title': banner_title,
    }
    return render(request, template_name, context)
