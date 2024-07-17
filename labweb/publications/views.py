from django.shortcuts import render
from .models import Publication
from django.db.models.functions import ExtractYear
from collections import defaultdict

def get_publications_by_team(request, team, pub_type, template_name):
    # 논문 데이터 가져오기
    publications = Publication.objects.filter(team=team, pub_type=pub_type.upper()).order_by('-published_date')

    # 연도별로 정리
    publications_by_year = defaultdict(list)
    for pub in publications:
        publications_by_year[pub.published_date.year].append(pub)

    context = {
        'publications_by_year': dict(publications_by_year),
        'pub_type': pub_type,
    }
    return render(request, template_name, context)

def ai_publications(request, pub_type):
    return get_publications_by_team(request, 'AI', pub_type, 'labweb/publication/ai_publications.html')

def hw_publications(request, pub_type):
    return get_publications_by_team(request, 'HW', pub_type, 'labweb/publication/hw_publications.html')
