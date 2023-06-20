from django.db import models

# Create your models here.



        #---------------- Titulo mision
class SurveyTitle(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    texto = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.titulo)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto para título de Encuestas"
        verbose_name_plural = "Texto para título de Encuestas"
        db_table = "survey_title_survey"
class Respuesta(models.Model):
    valor = models.CharField(max_length=200)
    orden = models.IntegerField(default=1)
    
    class Meta:
        ordering = ["orden"]

    def __str__(self):
        r = f'{str(self.valor)}'
        return r

class GrupoDeRespuestas(models.Model):
    nombre = models.TextField()
    respuestas = models.ManyToManyField(Respuesta, blank=True)
    tipo = models.CharField(max_length=30, choices=[('radio', 'Selección única'), ('checkbox', 'Selección múltiple'),('text', 'Cuadro de texto'), ('textarea','Área de texto'),
                                     ('date', 'Fecha'), ('email', 'Correo'), ('number', 'Número'), ('tel', 'Teléfono'), ('color', 'Color')])
    orden = models.IntegerField(default=1)
    
    def __str__(self):
        r = f'{str(self.nombre)}'
        return r
    
class Pregunta(models.Model):
    titulo = models.CharField(max_length=999)
    grupo_de_respuestas = models.ManyToManyField(GrupoDeRespuestas, blank=True, verbose_name='grupo de respuestas')
    orden = models.IntegerField(null=False)
    
    class Meta:
        ordering = ["orden", "titulo"]

    def __str__(self):
        return self.titulo

class Encuesta(models.Model):
    nombre = models.CharField(max_length=100)
    encabezado = models.TextField(blank=True)
    preguntas = models.ManyToManyField(Pregunta, blank=True)
    pie = models.TextField(blank=True, max_length=200)
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nombre




