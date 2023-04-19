from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Gallery


def index(request):
    photos = Gallery.objects.all()

    template = loader.get_template('../templates/labweb/gallery.html')
    context = {
            'photos': Gallery
        }
    return HttpResponse(template.render(context, request))
