from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Publication_list


def index(request):
    publications = Publication_list.objects.all()
    template = loader.get_template('../templates/labweb/publication.html')
    context = {
        'Publication_list': publications
    }
    return HttpResponse(template.render(context, request))


def detail(request, pub_id):
    return HttpResponse("You're looking at publication %s." % pub_id)
