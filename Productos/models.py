from django.db import models

# ---------------- Encabezado_Producto -------------------------------------------------------------------------

class Encabezado_Producto(models.Model):
    título = models.CharField(max_length=50)
    texto1 = models.TextField()
    texto2 = models.TextField()

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Encabezado Producto"
        verbose_name_plural = "Encabezado Producto"

# ---------------- Descripcion_Productos_Aicros -------------------------------------------------------------------------

class Descripcion_Productos_Aicros(models.Model):
    título = models.CharField(max_length=50)
    texto_1 = models.TextField()

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Descripción Productos Aicros"
        verbose_name_plural = "Descripción Productos Aicros"

# ---------------- Producto_Aicros -------------------------------------------------------------------------

class Producto_Aicros(models.Model):
    foto = models.ImageField(upload_to="Página Productos/Aicros/Imágenes/Imágenes", blank=True, null=False, default="../static/img/logo/aicros-logo.png")
    foto_carrusel = models.ImageField(upload_to="Página Productos/Aicros/Imágenes/Imágenes", blank=True, null=False, default="../static/img/logo/aicros-logo.png", verbose_name="Foto Carrusel")
    show = models.BooleanField(default=True, verbose_name="Mostrar en carrusel")
    show_text = models.BooleanField(default=True, verbose_name="Mostrar texto")
    show_image = models.BooleanField(default=True, verbose_name="Mostrar imagen")
    título = models.CharField(max_length=200, blank=True, null=True)
    resumen = models.TextField(max_length=200, default=título)
    descripción = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Productos/Aicros/Ícono", blank=True, null=False, default="../static/img/AicrosIdentificador.png"
    )
    nombre_Botón = models.CharField(max_length=30)

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Productos Aicros"
        verbose_name_plural = "Productos Aicros"

# ---------------- Descripcion_Productos_Distribuidos -------------------------------------------------------------------------

class Descripcion_Productos_Distribuidos(models.Model):
    título = models.CharField(max_length=50)
    texto_1 = models.TextField()

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Descripción Productos Distribuidos"
        verbose_name_plural = "Descripción Productos Distribuidos"

# ---------------- Producto_Distribuido_Aicros -------------------------------------------------------------------------

class Producto_Distribuido_Aicros(models.Model):
    foto = models.ImageField(
        upload_to="Página Productos/Aicros/Distribuidos/Imágenes", blank=True, null=False, default="../static/img/AicrosIdentificador.png"
    )
    foto_carrusel = models.ImageField(upload_to="Página Productos/Aicros/Distribuidos/Imágenes", blank=True, null=False, default="../static/img/logo/aicros-logo.png", verbose_name="Foto Carrusel")
    show = models.BooleanField(default=True, verbose_name="Mostrar en carrusel")
    show_text = models.BooleanField(default=True, verbose_name="Mostrar texto")
    show_image = models.BooleanField(default=True, verbose_name="Mostrar imagen")
    título = models.CharField(max_length=200, blank=True, null=True)
    resumen = models.TextField(max_length=200, default=título)
    descripción = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Productos/Aicros/Distribuidos/Ícono", blank=True, null=False, default="../static/img/AicrosIdentificador.png"
    )
    nombre_Botón = models.CharField(max_length=30)
    

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Producto Distribuido"
        verbose_name_plural = "Producto Distribuido"