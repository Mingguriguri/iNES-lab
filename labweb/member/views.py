from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render #new added


from .models import member_list

# 사용자 정의 정렬

def degree_weight(degree):
    if degree == 'Co-Advisor':
        return 1
    elif degree.startswith('Professor'):
        return 2
    elif degree =='PhD':
        return 3
    elif degree =='Master':
        return 4
    else:
        return 5

def index(request):
    members = member_list.objects.all()
    current_members = member_list.objects.filter(status='CU')
    alumni_members = member_list.objects.filter(status='AL')
    degrees = sorted(set(member.degree for member in member_list.objects.all()), key=degree_weight)
    template = loader.get_template('../templates/labweb/member.html')
    context = {
        'member_list': members,
        'current_members':current_members,
        'alumni_members':alumni_members,
    }
    return HttpResponse(template.render(context, request))

def filter_by_degree(request):
    degree = request.GET.get('degree', None)
    template = loader.get_template('../templates/labweb/member.html')

    if degree:
        filtered_members = member_list.objects.filter(degree=degree)
    else:
        filtered_members = member_list.objects.all()
    #degrees = sorted(set(member.degree for member in member_list.objects.all()), key=degree_weight)
    current_members = filtered_members.filter(status='CU')
    alumni_members = filtered_members.filter(status='AL')
    context = {
        'current_members':current_members,
        'alumni_members':alumni_members,
        'degree_choices': member_list.DEGREE_CHOICES,  # 템플릿에 전달
        'selected_degree': degree
    }
    return HttpResponse(template.render(context, request))    
    
