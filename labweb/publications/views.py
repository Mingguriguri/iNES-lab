from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Publication
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")