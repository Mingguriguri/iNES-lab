from django.shortcuts import render
from .models import member_list

# 사용자 정의 정렬 함수
def degree_weight(degree):
    if degree == 'Co-Advisor':
        return 1
    elif degree.startswith('Professor'):
        return 2
    elif degree == 'PhD':
        return 3
    elif degree == 'Master':
        return 4
    else:
        return 5

def ai_members(request):
    members = member_list.objects.filter(team='AI')
    current_members = members.filter(status='CU')
    alumni_members = members.filter(status='AL')
    context = {
        'member_list': members,
        'current_members': current_members,
        'alumni_members': alumni_members,
    }
    return render(request, 'labweb/member/ai_member.html', context)

def hw_members(request):
    members = member_list.objects.filter(team='HW')
    current_members = members.filter(status='CU')
    alumni_members = members.filter(status='AL')
    context = {
        'member_list': members,
        'current_members': current_members,
        'alumni_members': alumni_members,
    }
    return render(request, 'labweb/member/hw_member.html', context)

def ai_filter_by_degree(request):
    degree = request.GET.get('degree', None)
    if degree:
        filtered_members = member_list.objects.filter(degree=degree, team='AI')
    else:
        filtered_members = member_list.objects.filter(team='AI')
    current_members = filtered_members.filter(status='CU')
    alumni_members = filtered_members.filter(status='AL')
    context = {
        'current_members': current_members,
        'alumni_members': alumni_members,
        'degree_choices': member_list.DEGREE_CHOICES,
        'selected_degree': degree
    }
    return render(request, 'labweb/member/ai_member.html', context)

def hw_filter_by_degree(request):
    degree = request.GET.get('degree', None)
    if degree:
        filtered_members = member_list.objects.filter(degree=degree, team='HW')
    else:
        filtered_members = member_list.objects.filter(team='HW')
    current_members = filtered_members.filter(status='CU')
    alumni_members = filtered_members.filter(status='AL')
    context = {
        'current_members': current_members,
        'alumni_members': alumni_members,
        'degree_choices': member_list.DEGREE_CHOICES,
        'selected_degree': degree
    }
    return render(request, 'labweb/member/hw_member.html', context)
