from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models.functions import ExtractYear
from .models import Awards


def ai_award(request):
    awards = Awards.objects.all().order_by('-award_dates')
    awards = Awards.objects.filter(team='AI')
    template = loader.get_template('../templates/labweb/award/ai_awards.html.html')
    context = {
        'award_list': awards
    }
    return HttpResponse(template.render(context, request))


def hw_award(request):
    awards = Awards.objects.all().order_by('-award_dates')
    template = loader.get_template('../templates/labweb/award/award/hw_awards.html.html')
    context = {
        'award_list': awards
    }
    return HttpResponse(template.render(context, request))
