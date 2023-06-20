from django.shortcuts import render
from datetime import datetime
import os
from django.conf import settings
from django.core import mail
from django.core.mail import send_mail
from django.contrib import messages
from Encuestas.models import *
from Sweb.models import BannerTitle

# Create your views here.

def encuestaView(request, id=1):
    encuesta = Encuesta.objects.all().filter(id=id)[0]
    
    if request.method == 'POST':
        preguntas = {}
        date = datetime.now()

        for p in encuesta.preguntas.all():
            preguntas[p]=[]
            try:
                for g in p.grupo_de_respuestas.all():
                    if g.tipo == 'checkbox':
                        preguntas[p] +=  (request.POST.getlist(f'{p.id}{g.id}'))
                    else:
                        preguntas[p].append(request.POST[f'{p.id}{g.id}'])
            except Exception as e:
                print('respuesta vacia %s', e)
                preguntas[p]=''
        
        
        message = (f'Encuesta realizada en la fecha: {date} {os.linesep}{os.linesep}')
        for p in preguntas.keys():
            message += f'{os.linesep}{str(p)}{os.linesep}'
            for i in preguntas[p]:
                message += f'R/ {str(i)}{os.linesep}'
        try:
            with mail.get_connection() as connection:
                mail.EmailMessage(
                f'Encuesta {encuesta.nombre} portal Aicros',message,
                settings.EMAIL_HOST_USER,
                settings.EMAIL_RECEIVER,
                connection=connection,
                ).send()
            messages.success(request, 'Encuesta enviada!')
        except Exception as e:
            messages.error(request, 'Error al enviar encuesta')
            print(e) 
    
    
    return render(request, 'encuesta.html', {'encuesta':encuesta})

def encuestasView(request):
    banner_title = BannerTitle.objects.first()
    encuestas = Encuesta.objects.all()
    title = SurveyTitle.objects.all()
    context = {'encuestas': encuestas,
               'survey_title': title,
               'PaginaActual'  : "'Encuestas'",
               'banner_title': banner_title,}
    return render(request, 'encuestas.html', context)
