from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Projects, ProjectPhoto

def ai_projects_list(request):
    projects = Projects.objects.filter(team='AI').order_by('-end_date', '-start_date')  # 최신순으로 정렬
    paginator = Paginator(projects, 5)  # 페이지당 5개의 프로젝트를 표시
    page = request.GET.get('page')
    projects = paginator.get_page(page)

    # 각 프로젝트에 첫 번째 이미지를 추가
    for project in projects:
        project.first_photo = project.photos.first()

    context = {
        'projects': projects,
    }
    return render(request, 'labweb/project/ai_projects_list.html', context)

def hw_projects_list(request):
    projects = Projects.objects.filter(team='HW').order_by('-end_date', '-start_date')  # 최신순으로 정렬
    paginator = Paginator(projects, 5)  # 페이지당 5개의 프로젝트를 표시
    page = request.GET.get('page')
    projects = paginator.get_page(page)

    # 각 프로젝트에 첫 번째 이미지를 추가
    for project in projects:
        project.first_photo = project.photos.first()

    context = {
        'projects': projects,
    }
    return render(request, 'labweb/project/hw_projects_list.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    keywords = project.keywords.split(',') if project.keywords else []
    photos = project.photos.all()
    context = {
        'project': project,
        'keywords': keywords,
        'photos': photos,
    }
    return render(request, 'labweb/project/project_detail.html', context)
