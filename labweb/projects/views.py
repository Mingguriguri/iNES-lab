from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import article_list

# Create your views here.
def index(request):
    articles = article_list.objects.all()
    template = loader.get_template('../templates/labweb/projects.html')
    for article in articles:
        if len(article.article_abstract) > 150:
            article.article_abstract = article.article_abstract[:150] + "..."

    context = {
        'article_list': articles
    }
    return HttpResponse(template.render(context, request))

# def detail(request, article_id):
#     return HttpResponse("You're looking at article %s." % article_id)

def detail(request, article_id):
    article = get_object_or_404(article_list, pk=article_id)
    template = loader.get_template('../templates/labweb/detail.html')
    keywords = article.article_keywords.split(';')
    context = {
        'article': article,
        'keywords': keywords
    }
    
    return HttpResponse(template.render(context, request))

def topic(request):
    template = loader.get_template('../templates/labweb/research_topic.html')
    return HttpResponse(template.render({}, request))