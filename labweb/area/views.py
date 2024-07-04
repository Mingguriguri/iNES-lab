from django.shortcuts import render
from .models import Area

def ai_research_topic(request):
    areas = Area.objects.filter(team='AI')
    return render(request, 'labweb/research_topic/ai_research_topic.html', {'areas': areas})

def hw_research_topic(request):
    areas = Area.objects.filter(team='HW')
    return render(request, 'labweb/research_topic/hw_research_topic.html', {'areas': areas})
