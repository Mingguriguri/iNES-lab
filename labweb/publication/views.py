from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models.functions import ExtractYear
from .models import Journal, Conference


def index(request):
    publications = Journal.objects.order_by('-pub_dates').annotate(year=ExtractYear('pub_dates')).order_by('-year', '-pub_dates')
    years = set([p.year for p in publications])
    template = loader.get_template('../templates/labweb/publication.html')
    context = {
        'years': sorted(years, reverse=True),
        'Publication_list': publications
    }
    return HttpResponse(template.render(context, request))


def detail(request, pub_id):
    return HttpResponse("You're looking at publication %s." % pub_id)

def conference(request):
    conferences = Conference.objects.order_by('-conf_dates').annotate(year=ExtractYear('conf_dates')).order_by('-year', '-conf_dates')
    years = set([c.year for c in conferences])
    template = loader.get_template('../templates/labweb/conference.html')
    context = {
        'years': sorted(years, reverse=True),
        'conferences': conferences
    }
    return HttpResponse(template.render(context, request))
