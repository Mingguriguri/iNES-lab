from django.shortcuts import render
from .models import Publication
from django.db.models.functions import ExtractYear

def ai_publications(request, pub_type):
    # 논문 데이터 가져오기
    publications = Publication.objects.filter(team='AI', pub_type=pub_type.upper()).order_by('-published_date')
    
    # 연도별로 정리
    years = publications.annotate(year=ExtractYear('published_date')).values_list('year', flat=True).distinct()
    
    # 저자 포맷팅
    for pub in publications:
        authors = pub.authors.all()
        if authors.count() == 1:
            pub.formatted_authors = authors.first().name
        else:
            author_names = [author.name for author in authors]
            pub.formatted_authors = ', '.join(author_names[:-1]) + ' and ' + author_names[-1]
    
    context = {
        'publications': publications,
        'years': years,
        'pub_type': pub_type,
    }
    return render(request, 'labweb/publication/ai_publications.html', context)



def hw_publications(request, pub_type):
    # 논문 데이터 가져오기
    publications = Publication.objects.filter(team='HW', pub_type=pub_type.upper()).order_by('-published_date')
    
    # 연도별로 정리
    years = publications.annotate(year=ExtractYear('published_date')).values_list('year', flat=True).distinct()
    
    # 저자 포맷팅
    for pub in publications:
        authors = pub.authors.all()
        if authors.count() == 1:
            pub.formatted_authors = authors.first().name
        else:
            author_names = [author.name for author in authors]
            pub.formatted_authors = ', '.join(author_names[:-1]) + ' and ' + author_names[-1]
    
    context = {
        'publications': publications,
        'years': years,
        'pub_type': pub_type,
    }
    return render(request, 'labweb/publication/ai_publications.html', context)

