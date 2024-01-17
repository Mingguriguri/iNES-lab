from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import History

def index(request):
    historys = History.objects.all().order_by('-history_date') #역순 정렬(최신 우선)

    
    template = loader.get_template('../templates/labweb/history.html')
    context = {
        'historys' : historys,
    }   
    return HttpResponse(template.render(context, request))