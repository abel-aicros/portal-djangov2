"""
Django settings for Aicros project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# MEDIA_ROOT = os.path.join(BASE_DIR, 'Files')
# MEDIA_URL = '/Files/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3+-pi=go@1l=+fx4t+8idyl$ou(12kv@m!7^=x$!m+36=cf7a)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DATA_UPLOAD_MAX_MEMORY_SIZE = 10*1024*1024

ALLOWED_HOSTS = ["*"]
# Application definition
INSTALLED_APPS = [
    # 'adminlte3',
    # 'adminlte3_theme',
    'jazzmin',
    # 'fontawesomefree',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'Sweb',
    'Nosotros',
    'Productos',
    'Servicios',
    'Documentos',
    'Encuestas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
]

ROOT_URLCONF = 'Aicros.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Aicros.wsgi.application'

CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000/", "http://*.cu", "https://*.cu", "https://aicros.cu'"]
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'portaldb',
    'USER': 'abel-aicros',
    'PASSWORD': 'R2Gy7TaJqHLo',
    'HOST': 'ep-misty-frog-305205.us-east-2.aws.neon.tech',
    'PORT': '5432',
  }
}

# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     #'NAME': 'portalv2test',
#     'NAME': 'portaldb',
#     'USER': 'postgres',
#     'PASSWORD': 'postgres',
#     'HOST': 'localhost',
#     'PORT': '5432',
#   }
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

STATIC_ROOT = 'static_Server'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Mailtrap

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
# EMAIL_HOST_USER = '347c4fec4c9616'
# EMAIL_HOST_PASSWORD = '639acaac02b6f7'
# EMAIL_PORT = '2525'


# Gmail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'correo@gmail.com'
# EMAIL_HOST_PASSWORD = '12345678'


#Aicros
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'zimbra.aicros.cu'
EMAIL_HOST_USER = 'portal.aicros@aicros.cu'
EMAIL_HOST_PASSWORD = 'P0rt@lDjango2023*'
EMAIL_PORT = '465'
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True 
EMAIL_RECEIVER = [ 'abeldarrain@aicros.cu']
# EMAIL_RECEIVER = ['aicros@aicros.cu', 'comercial@aicros.cu', 'abeldarrain@aicros.cu']


# JAZZMIN SETTINGS
JAZZMIN_SETTINGS = {
    "site_title": "Web",
    "site_header": "Sitio Web Aicros",
    "site_brand": "Aicros",
    "site_icon": "images/favicon.png",
    # Add your own branding here
    "site_logo": "img/AicrosIdentificador.png",
    # "login_logo": "books/img/logo-login.png",
    "welcome_sign": "Administración aicros",
    # Copyright on the footer
    "copyright": "www.aicros.cu",
    "user_avatar": None,
    "search_model": "Productos.Producto_Aicros",
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Inicio", "url": "http://127.0.0.1:8000", "permissions": ["auth.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        {'app': 'Sweb'},
        {'app': 'Nosotros'},
        {'app': 'Productos'},
        {'app': 'Servicios'},
        {'app': 'Documentos'},
        {'app': 'Encuestas'},
    ],
    ############
    # Side Menu #
    ############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-users",
        # "Sweb.LogEntry": "fas fa-users",
    },

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        
        "auth",

        "Sweb.Carrusel",
        "Sweb.InicioProducto",
        "Sweb.Carrusel_Productos",
        "Sweb.InicioServicio",
        "Sweb.Carrusel_Servicios",
        "Sweb.Líneas_de_Negocio",
        "Sweb.Cifra",
        "Sweb.Noticia_1",
        "Sweb.Noticia_2",
        "Sweb.Noticia_3",
        "Sweb.Alianza",

        "Nosotros.Encabezado_Nosotros",
        "Nosotros.Mision_Nosotros",
        "Nosotros.Vision_Nosotros",
        "Nosotros.Valores_Nosotros",
        "Nosotros.Anno_Historia",
        "Nosotros.Miembro_de_Trabajo",
        "Nosotros.Evento_Columna_1",
        "Nosotros.Encabezado_Nosotros",
        "Nosotros.Encabezado_Nosotros",

        "Productos.Encabezado_Producto",
        "Productos.Descripcion_Productos_Aicros",
        "Productos.Producto_Aicros",
        "Productos.Descripcion_Productos_Distribuidos",
        "Productos.Producto_Distribuido_Aicros",

        "Servicios.Encabezado_Servicio",
        "Servicios.Descripcion_Servicios_Aicros",
        "Servicios.Servicio_Aicros",
        
        "Documentos.Encabezado_Documentos",
        "Documentos.Texto_Documentos_Rapidos",
        "Documentos.Documentos_de_Rápido_Acceso",
        "Documentos.Contrato_General_Columna_1",
        "Documentos.Contrato_General_Columna_2",
        "Documentos.Contrato_General_Columna_3",
        "Documentos.Contrato_Específico_Columna_1",
        "Documentos.Contrato_Específico_Columna_2",
        "Documentos.Contrato_Específico_Columna_3",
        "Documentos.Listado_Productos_y_Servicios_Columna_1",
        "Documentos.Listado_Productos_y_Servicios_Columna_2",
        "Documentos.Listado_Productos_y_Servicios_Columna_3",
        "Documentos.Registro_y_Certificaciones_de_Software_CENDA_Columna_1",
        "Documentos.Registro_y_Certificaciones_de_Software_CENDA_Columna_2",
        "Documentos.Registro_y_Certificaciones_de_Software_CENDA_Columna_3",
        "Documentos.Registro_y_Certificaciones_de_Software_MICONS_Columna_1",
        "Documentos.Registro_y_Certificaciones_de_Software_MICONS_Columna_2",
        "Documentos.Registro_y_Certificaciones_de_Software_MICONS_Columna_3",
        "Documentos.Registro_y_Certificaciones_de_Software_Otros_Documentos_Columna_1",
        "Documentos.Registro_y_Certificaciones_de_Software_Otros_Documentos_Columna_2",
        "Documentos.Registro_y_Certificaciones_de_Software_Otros_Documentos_Columna_3",
        ],

    # # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # Uncomment this line once you create the bootstrap-dark.css file
    "custom_css": "css/bootstrap-dark.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
    
    "theme": "default",  
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",

    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    }
}

from django.http import HttpResponse
HttpResponse.mimetype['css'] = 'text/css'