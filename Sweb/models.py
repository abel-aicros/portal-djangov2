from django.db import models
from colorfield.fields import ColorField
import datetime
import django

 #---------------- Titulo banner
class BannerTitle(models.Model):
    texto = models.CharField(max_length=100, blank=True, null=True)
    texto_negrita = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto para título de Banner"
        verbose_name_plural = "Texto para título de Banner"
        
 #---------------- Titulo promociones
class PromotionsTitle(models.Model):
    texto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto para título de Promociones"
        verbose_name_plural = "Texto para título de Promociones"
        db_table = "index_title_promotions"
   


# ---------------- Carrusel -------------------------------------------------------------------------



class Carrusel(models.Model):
    texto = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to="productosFotos", blank=True, null=True)

    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Ímagen_para_Carrusel_de_Promociones"
        verbose_name_plural = "Ímagen_para_Carrusel_de_Promociones"
        db_table = "Ímagen_para_Carrusel_de_Promociones"

        
# ---------------- InicioProducto -------------------------------------------------------------------------
class InicioProducto(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["id"]
        verbose_name = "Caja Productos"
        verbose_name_plural = "Caja Productos"
        # db_table = "Caja Productos"


        

# ---------------- InicioServicio -------------------------------------------------------------------------

class InicioServicio(models.Model):
    título = models.CharField(max_length=50, blank=True, null=True)
    descripción = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Caja_de_Servicios"
        verbose_name_plural = "Caja_de_Servicios"
        db_table = "Caja_de_Servicios"


        #---------------- Titulo lineas
class BussinesLinesTitle(models.Model):
    texto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto para título de Lineas de negocio"
        verbose_name_plural = "Texto para título de Lineas de negocio"
        db_table = "index_title_buss_lines"

# ---------------- Líneas_de_Negocio -------------------------------------------------------------------------

class Líneas_de_Negocio(models.Model):
    ícono = models.ImageField(
        upload_to="Página Home/Líneas de Negocio/Ícono", blank=True, null=True
    )
    descripción = models.TextField()

    def __str__(self):
        return str(self.descripción)

    class Meta:
        ordering = ["id"]
        verbose_name = "Línea de Negocio"
        verbose_name_plural = "Línea de Negocio"

        #---------------- Titulo cifras
class StatsTitle(models.Model):
    texto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto para título de La empresa en cifras"
        verbose_name_plural = "Texto para título de La empresa en cifras"
        db_table = "index_title_stats"

# ---------------- Cifra -------------------------------------------------------------------------

class Cifra(models.Model):
    título = models.CharField(max_length=200)
    número = models.CharField(max_length=50)
    color = ColorField(default='#991A14')
    font_color = ColorField(default='#FFFF')

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["título"]
        verbose_name = "Cifra"
        verbose_name_plural = "Cifra"
        # db_table = "cifra"

        #---------------- Titulo noticias
class NewsTitle(models.Model):
    texto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto para título de Noticias"
        verbose_name_plural = "Texto para título de Noticias"
        db_table = "index_title_news"
# ---------------- Noticia -------------------------------------------------------------------------

class Noticia(models.Model):
    título = models.CharField(max_length=150, default="Nueva Noticia")
    foto = models.ImageField(upload_to="Página Home/Noticias/", default="../static/img/AicrosIdentificador.png")
    Introducción_de_Noticia = models.TextField(max_length=200)
    Continuación_de_Noticia = models.TextField()
    Fecha = models.DateField(default=django.utils.timezone.now)
    show = models.BooleanField(default=True, verbose_name="Mostrar Noticia")
    
    Introducción_de_Noticia_parsed = ''

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["-Fecha"]
        verbose_name = "Noticia"
        verbose_name_plural = "Noticia"


        #---------------- Titulo alianzas
class AllianceTitle(models.Model):
    texto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto para título de Alianzas"
        verbose_name_plural = "Texto para título de Alianzas"
        db_table = "index_title_alliance"
# ---------------- Alianza -------------------------------------------------------------------------

class Alianza(models.Model):
    nombre = models.CharField(max_length=100, default="Alianza de Aicros")
    foto = models.ImageField(upload_to="Página Home/Alianzas/Ímagen", blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["id"]
        verbose_name = "Alianza"
        verbose_name_plural = "Alianza"
        
        #--------------------------Text404
class Page404(models.Model):
    texto = models.CharField(max_length=100, default="Página no encontrada!")
    foto = models.ImageField(upload_to="Página Home/", blank=True, null=False, default='../static/img/logo/invertido.png')
    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "página 404"