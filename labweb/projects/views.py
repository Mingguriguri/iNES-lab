from django.http import HttpResponse
from django.template import loader

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
    template = loader.get_template('../templates/labweb/projects.html')

    return HttpResponse(template.render(context, request))

def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)

