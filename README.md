# 2209-Portal_django

#Portal web de la empresa aicros

== Alojar base de datos (portaldb.backup) en un servidor y modificar los siguientes atributos de la variable DATABASES en el directorio Aicros/settings.py

DATABASES = {
  'default': {
    <-- ENGINE dejar como está -->
    'NAME': 'nombre de base de datos',
    'USER': 'usuario de base de datos',
    'PASSWORD': 'contrasena de usuario',
    'HOST': 'localhost',
    'PORT': '5432',
  }
}

== Eliminar base de datos de repositorio y desplegar el resto 

==python v 3.11
==librerias en requirements.txt