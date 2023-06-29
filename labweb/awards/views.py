from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models.functions import ExtractYear
from .models import Awards


def index(request):
    awards = Awards.objects.all().order_by('-award_dates')
    template = loader.get_template('../templates/labweb/awards.html')
    context = {
        'award_list': awards
    }
    return HttpResponse(template.render(context, request))
