from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render #new added


from .models import member_list

# 사용자 정의 정렬
def degree_weight(degree):
    if degree == 'Advisor':
        return 1
    elif degree.startswith('Professor'):
        return 2
    elif degree =='Ph.D. student':
        return 3
    elif degree =='M.S. student':
        return 4
    else:
        return 5

def index(request):
    members = member_list.objects.all()
    degrees = sorted(set(member.degree for member in member_list.objects.all()), key=degree_weight)
    template = loader.get_template('../templates/labweb/member.html')
    context = {
        'member_list': members
    }
    return HttpResponse(template.render(context, request))

def filter_by_degree(request):
    degree = request.GET.get('degree', None)
    template = loader.get_template('../templates/labweb/member.html')

    if degree:
        members = member_list.objects.filter(degree=degree)
    else:
        members = member_list.objects.all()
    degrees = sorted(set(member.degree for member in member_list.objects.all()), key=degree_weight)

    context = {
        'member_list': members,
        'degrees': degrees,
        'selected_degree': degree
    }
    return HttpResponse(template.render(context, request))    
    
