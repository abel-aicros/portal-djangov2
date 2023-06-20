from django.contrib import admin
from .models import *

# Register your models here.

# --------------------Página Productos--------------------
admin.site.register(Encabezado_Producto)
admin.site.register(Producto_Aicros)
admin.site.register(Producto_Distribuido_Aicros)
admin.site.register(Descripcion_Productos_Aicros)
admin.site.register(Descripcion_Productos_Distribuidos)