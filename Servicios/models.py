from django.db import models
from Sweb.models import Líneas_de_Negocio

# ---------------- Encabezado_Servicio -------------------------------------------------------------------------

class Encabezado_Servicio(models.Model):
    título = models.CharField(max_length=50)
    texto_1 = models.TextField()
    texto_2 = models.TextField()

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Encabezado Servicio"
        verbose_name_plural = "Encabezado Servicio"

# ---------------- Descripcion_Servicios_Aicros -------------------------------------------------------------------------

class Descripcion_Servicios_Aicros(models.Model):
    título = models.CharField(max_length=50)
    texto_1 = models.TextField()

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Descripción Servicio Aicros"
        verbose_name_plural = "Descripción Servicio Aicros"

# ---------------- Servicio_Aicros -------------------------------------------------------------------------

class Servicio_Aicros(models.Model):
    foto_carrusel = models.ImageField(upload_to="Página Servicios/Servicios", blank=True, null=False, verbose_name="Foto Carrusel", default="../static_Server/img/logo/aicros-logo.jpg")
    show = models.BooleanField(default=True, verbose_name="Mostrar en carrusel")
    show_text = models.BooleanField(default=True, verbose_name="Mostrar texto")
    show_image = models.BooleanField(default=True, verbose_name="Mostrar imagen")
    descripción = models.TextField()
    line_id = models.ForeignKey(Líneas_de_Negocio, on_delete=models.CASCADE, verbose_name="Línea de negocio")

    def __str__(self):
        return str(self.descripción)

    class Meta:
        ordering = ["id"]
        verbose_name = "Servicio Aicros"
        verbose_name_plural = "Servicio Aicros"

