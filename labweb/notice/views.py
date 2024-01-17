from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage # 페이지네이셔
from .models import Notice


def notice_list(request):
    all_notices = Notice.objects.all().order_by('-created_at')
    page        = request.GET.get('page')
    paginator   = Paginator(all_notices, 5) #Painator(쿼리셋, 한 페이지에 몇 개의 포스트를 볼 지)
    notices     = paginator.get_page(page)

    try:      
        page_obj = paginator.page(page) #Paginator객체 (뒤에 현재 페이지가 몇 페이지인지 나타냄)
    except PageNotAnInteger: #페이지를 입력하지 않을 시 발생되는 문제 
        page     = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page    = paginator.num_pages #가장 마지막 page를 추출하여 갱신
        page_obj = paginator.page(page)
    
    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    
    custom_range = range(leftIndex, rightIndex+1)
    
    template = loader.get_template('../templates/labweb/notice.html')
    context = {
        'notices': notices,
        'page_obj':page_obj,
        'paginator': paginator,
        'custom_range': custom_range,
    }
    return HttpResponse(template.render(context, request))


def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    try:
        prev_notice = Notice.objects.filter(id__lt=notice_id).order_by('-id').first()
    except Notice.DoesNotExist:
        prev_notice = None

    try:
        next_notice = Notice.objects.filter(id__gt=notice_id).order_by('id').first()
    except Notice.DoesNotExist:
        next_notice = None
    context = {
        'notice': notice,
        'prev_notice':prev_notice,
        'next_notice':next_notice,
    }

    return render(request, '../templates/labweb/notice_detail.html', context)