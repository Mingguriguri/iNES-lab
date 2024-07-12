from django.shortcuts import render
from .models import member_list
import logging

# 로거 설정
logger = logging.getLogger(__name__)

# 사용자 정의 정렬 함수
def degree_weight(degree):
    """학위(degree)에 따라 가중치를 반환하는 함수"""
    if degree == 'CA':  # Co-Advisor
        return 1
    elif degree == 'PR':  # Professor
        return 2
    elif degree == 'PD':  # Postdoc
        return 3
    elif degree == 'RS':
        return 4
    elif degree == 'PHD':  # PhD
        return 5
    elif degree == 'MS':  # Master
        return 6
    else:  # BS: Bachelor
        return 7

def ai_members(request):
    """AI 팀 멤버를 학위 순서와 입력 날짜 순서로 정렬하여 반환"""
    members = list(member_list.objects.filter(team='AI'))
    logger.debug(f"Members before sorting: {[member.degree for member in members]}")
    members.sort(key=lambda member: (degree_weight(member.degree), member.id))  # 학위 순서와 입력 날짜 순서로 정렬
    logger.debug(f"Members after sorting: {[member.degree for member in members]}")
    current_members = [m for m in members if m.status == 'CU']
    alumni_members = [m for m in members if m.status == 'AL']
    context = {
        'member_list': members,
        'current_members': current_members,
        'alumni_members': alumni_members,
    }
    return render(request, 'labweb/member/ai_member.html', context)

def hw_members(request):
    """HW 팀 멤버를 학위 순서와 입력 날짜 순서로 정렬하여 반환"""
    members = list(member_list.objects.filter(team='HW'))
    logger.debug(f"Members before sorting: {[member.degree for member in members]}")
    members.sort(key=lambda member: (degree_weight(member.degree), member.id))  # 학위 순서와 입력 날짜 순서로 정렬
    logger.debug(f"Members after sorting: {[member.degree for member in members]}")
    current_members = [m for m in members if m.status == 'CU']
    alumni_members = [m for m in members if m.status == 'AL']
    context = {
        'member_list': members,
        'current_members': current_members,
        'alumni_members': alumni_members,
    }
    return render(request, 'labweb/member/hw_member.html', context)

def ai_filter_by_degree(request):
    """AI 팀 멤버를 학위 기준으로 필터링하고 정렬하여 반환"""
    degree = request.GET.get('degree', None)
    if degree:
        filtered_members = list(member_list.objects.filter(degree=degree, team='AI'))
    else:
        filtered_members = list(member_list.objects.filter(team='AI'))
    filtered_members.sort(key=lambda member: (degree_weight(member.degree), member.id))  # 학위 순서와 입력 날짜 순서로 정렬
    current_members = [m for m in filtered_members if m.status == 'CU']
    alumni_members = [m for m in filtered_members if m.status == 'AL']
    context = {
        'current_members': current_members,
        'alumni_members': alumni_members,
        'degree_choices': member_list.DEGREE_CHOICES,
        'selected_degree': degree
    }
    return render(request, 'labweb/member/ai_member.html', context)

def hw_filter_by_degree(request):
    """HW 팀 멤버를 학위 기준으로 필터링하고 정렬하여 반환"""
    degree = request.GET.get('degree', None)
    if degree:
        filtered_members = list(member_list.objects.filter(degree=degree, team='HW'))
    else:
        filtered_members = list(member_list.objects.filter(team='HW'))
    filtered_members.sort(key=lambda member: (degree_weight(member.degree), member.id))  # 학위 순서와 입력 날짜 순서로 정렬
    current_members = [m for m in filtered_members if m.status == 'CU']
    alumni_members = [m for m in filtered_members if m.status == 'AL']
    context = {
        'current_members': current_members,
        'alumni_members': alumni_members,
        'degree_choices': member_list.DEGREE_CHOICES,
        'selected_degree': degree
    }
    return render(request, 'labweb/member/hw_member.html', context)
