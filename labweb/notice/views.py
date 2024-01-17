from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Notice


def index(request):
    notices = Notice.objects.all().order_by('-created_at')
    template = loader.get_template('../templates/labweb/notice.html')
    context = {
        'notices': notices,
    }
    return HttpResponse(template.render(context, request))
