from django.db import models

# ---------------- Encabezado_Documentos -------------------------------------------------------------------------

class Encabezado_Documentos(models.Model):
    título = models.CharField(max_length=50)
    texto_1 = models.TextField()
    texto_2 = models.TextField()

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Encabezado Documento"
        verbose_name_plural = "Encabezado Documento"

# ---------------- Texto_Documentos_Rapidos -------------------------------------------------------------------------

class Texto_Documentos_Rapidos(models.Model):
    título = models.CharField(max_length=50, blank=False)
    texto = models.TextField()

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto Documentos Rápidos"
        verbose_name_plural = "Texto Documentos Rápidos"

#------------------------------ doc rapidos

class DocumentoRap(models.Model):
    nombre = models.CharField(max_length=500)
    doc_file = models.FileField(
        upload_to="Página Documentos/Documentos",verbose_name='Archivos', default="Página Documentos/Documentos/default.docx", blank=False,
    )


    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Documento rápido" 
        verbose_name_plural = "Documentos rápidos"
        managed=True
        

#------------------------Secciones de Document
class Seccion(models.Model):
    texto = models.CharField(max_length=100, blank=False, null=False, default='Sección de Documentos')

    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Seccion de documentos"
        verbose_name_plural = "Secciones de documentos"
        db_table = "section"
        managed=True

# ---------------- Documentos-------------------------------------------------------------------------

class Documento(models.Model):
    nombre = models.CharField(max_length=500)
    doc_file = models.FileField(
        upload_to="Página Documentos/Documentos", verbose_name='Archivo', default="Página Documentos/Documentos/default.docx",blank=False,
    )
    seccion =  models.ManyToManyField(Seccion, blank=False,verbose_name='sección')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        db_table = "documento"
        verbose_name = "Documento" 
        managed=True
        


# ---------------- Contrato_General_Columna_1 