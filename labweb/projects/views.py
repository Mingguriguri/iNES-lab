from django.http import HttpResponse
from django.template import loader

from .models import article_list

# Create your views here.
def index(request):
    articles = article_list.objects.all()
    template = loader.get_template('projects/index.html')
    context = {
        'article_list': articles
    }
    return HttpResponse(template.render(context, request))