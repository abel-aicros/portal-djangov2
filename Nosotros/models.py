from django.db import models

# ---------------- Encabezado_Nosotros -------------------------------------------------------------------------

class Encabezado_Nosotros(models.Model):
    título = models.CharField(max_length=50)
    texto_1 = models.TextField()
    texto_2 = models.TextField()

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Encabezado Nosotros"
        verbose_name_plural = "Encabezado Nosotros"

        #---------------- Titulo mision
class MissionTitle(models.Model):
    texto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto para título de Mision, Vision y Valores"
        verbose_name_plural = "Texto para título de Mision, Vision y Valores"
        db_table = "about_us_title_mission"
        
# ---------------- Mision_Nosotros -------------------------------------------------------------------------

class Mision_Nosotros(models.Model):
    título = models.CharField(max_length=50)
    descripción = models.TextField()

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Misión"
        verbose_name_plural = "Misión"

# ---------------- Vision_Nosotros -------------------------------------------------------------------------

class Vision_Nosotros(models.Model):
    título = models.CharField(max_length=50)
    descripción = models.TextField()

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Visión"
        verbose_name_plural = "Visión"

# ---------------- Valores_Nosotros -------------------------------------------------------------------------

class Valores_Nosotros(models.Model):
    título = models.CharField(max_length=50)
    descripción = models.TextField()

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["id"]
        verbose_name = "Valores"
        verbose_name_plural = "Valores"
        
 #-----------------Titulo Historia
class HistoryTitle(models.Model):
    texto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto para título de Historia"
        verbose_name_plural = "Texto para título de Historia"
        db_table = "about_us_title_history"
        
        
# ---------------- Anno_Historia -------------------------------------------------------------------------

class Anno_Historia(models.Model):
    número = models.IntegerField()
    descripción = models.TextField()

    def __str__(self):
        return str(self.número)

    class Meta:
        ordering = ["número"]
        verbose_name = "Año de Historia"
        verbose_name_plural = "Año de Historia"
#-0-----------------------Cronologia
class TimeLapse(models.Model):
    fyear = models.CharField(default='', max_length=8, blank=True, verbose_name='año de inicio')
    lyear = models.CharField(default='', max_length=8, blank=True, verbose_name='año de fin')

    def __str__(self):
        return str(self.fyear) + "..." + str(self.lyear)

    class Meta:
        ordering = ["fyear"]
        verbose_name = "Cronología"
        verbose_name_plural = "Cronología"

#-----------------Titulo workteam
class WorkTeamTitle(models.Model):
    texto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto para título de Equipo de trabajo"
        verbose_name_plural = "Texto para título de Equipo de trabajo"
        db_table = "about_us_title_workteam"
        
      
# ---------------- Miembro_de_Trabajo -------------------------------------------------------------------------

class Miembro_de_Trabajo(models.Model):
    foto = models.ImageField(
        upload_to="Página Nosotros/Miembro de Trabajo/Imágenes", blank=True, null=True
    )
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["id"]
        verbose_name = "Miembro de Trabajo"
        verbose_name_plural = "Miembro de Trabajo"
        
#-----------------Titulo Historia
class EventsTitle(models.Model):
    texto = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.texto)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto para título de Eventos"
        verbose_name_plural = "Texto para título de Eventos"
        db_table = "about_us_title_events"
        
      

# ---------------- Eventos -------------------------------------------------------------------------

class Evento(models.Model):
    título = models.CharField(max_length=50)
    descripción = models.TextField(max_length=430)

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["título"]
        verbose_name = "Evento"
        verbose_name_plural = "Evento"