from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models.functions import ExtractYear
from .models import Publication_list


def index(request):
    publications = Publication_list.objects.order_by('-pub_dates').annotate(year=ExtractYear('pub_dates')).order_by('-year', '-pub_dates')
    years = set([p.year for p in publications])
    template = loader.get_template('../templates/labweb/publication.html')
    context = {
        'years': sorted(years, reverse=True),
        'Publication_list': publications
    }
    return HttpResponse(template.render(context, request))


def detail(request, pub_id):
    return HttpResponse("You're looking at publication %s." % pub_id)
