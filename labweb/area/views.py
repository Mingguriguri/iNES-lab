from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Area

def topic(request):
    areas = Area.objects.all()  # Projects 모든 인스턴스 가져오기
    template = loader.get_template('../templates/labweb/research_topic.html')
    context = {
        'areas': areas,
    }
    return HttpResponse(template.render(context, request))