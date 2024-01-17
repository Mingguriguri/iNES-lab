from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Projects

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def projects_list(request):
    projects = Projects.objects.all()  # Projects 모든 인스턴스 가져오기
    template = loader.get_template('../templates/labweb/projects_list.html')
    context = {
        'projects': projects,
    }
    return HttpResponse(template.render(context, request))