from django.shortcuts import render
from django.views import View

from Sweb.models import BannerTitle
from .models import *
from datetime import date



# Create your views here.


def aboutView(request):
    template_name = "Nosotros/nosotros.html"

    banner_title = BannerTitle.objects.first()
    encabezado_nosotros = Encabezado_Nosotros.objects.all()
    mision_nosotros = Mision_Nosotros.objects.all()
    vision_nosotros = Vision_Nosotros.objects.all()
    valores_nosotros = Valores_Nosotros.objects.all()
    anno_historia = Anno_Historia.objects.all()
    time_lapses = TimeLapse.objects.all()
    miembro_de_trabajo = Miembro_de_Trabajo.objects.all()
    evento = Evento.objects.all()
    
    title_mission = MissionTitle.objects.all()
    title_history = HistoryTitle.objects.all()
    title_workteam = WorkTeamTitle.objects.all()
    title_events = EventsTitle.objects.all()

    from itertools import chain
    mvv = list(chain(mision_nosotros, vision_nosotros, valores_nosotros))
    
    history_by_lapse = {}
    current_year = date.today().year
    for i in list(time_lapses):
        fyear = 0 if not i.fyear else int(i.fyear)
        lyear = current_year if not i.lyear else int(i.lyear)
        print(fyear,lyear)
        history_by_lapse[i] = []
        for j in list(anno_historia):
            if fyear <= int(str(j)) <= lyear:
                history_by_lapse[i].append(j)

    
    context = {
        'Encabezado_Nosotros': encabezado_nosotros,
        'Mision_Nosotros': mision_nosotros,
        'Vision_Nosotros': vision_nosotros,
        'Valores_Nosotros': valores_nosotros,
        'Anno_Historia': anno_historia,
        'Miembro_de_Trabajo': miembro_de_trabajo,
        'Evento': evento,
        
        'title_mission': title_mission,
    'title_history': title_history,
    'title_workteam': title_workteam,
    'title_events': title_events,
    'mvv': mvv,
    'time_lapses': time_lapses,
    'history_by_lapse': history_by_lapse,
    'banner_title': banner_title,
    'PaginaActual'  : "'Nosotros'",
         }

    return render(request, template_name, context)
