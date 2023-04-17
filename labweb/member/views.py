from django.http import HttpResponse
from django.template import loader

from .models import member_list

def index(request):
    members = member_list.objects.all()
    template = loader.get_template('../templates/labweb/member.html')
    context = {
        'member_list': members
    }
    return HttpResponse(template.render(context, request))