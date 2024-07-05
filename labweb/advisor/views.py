from django.shortcuts import render
from .models import Advisor
from project.models import Projects
from publications.models import Publication

def advisor_list(request, team):
    advisors = Advisor.objects.filter(team=team.upper())
    team_name = "AI" if team.lower() == "ai" else "HW"
    
    # 김정석 교수님을 조건에 따라 추가
    if team.lower() in ['ai', 'hw']:
        jeongseok_professor = Advisor.objects.filter(name="Jungsuk Kim", team="HW").first()
        if jeongseok_professor and jeongseok_professor not in advisors:
            advisors = list(advisors) + [jeongseok_professor]
    
    for advisor in advisors:
        advisor.keywords_list = advisor.keywords.split(',')

    # 최근 상위 5개의 프로젝트와 출판물 가져오기
    recent_projects = Projects.objects.filter(team=team.upper()).order_by('-start_date')[:5]
    recent_publications = Publication.objects.filter(team=team.upper()).order_by('-published_date')[:5]

    context = {
        'advisors': advisors,
        'team': team_name,
        'recent_projects': recent_projects,
        'recent_publications': recent_publications
    }
    return render(request, 'labweb/advisor/advisor_list.html', context)
