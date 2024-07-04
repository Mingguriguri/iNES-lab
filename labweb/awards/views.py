from django.shortcuts import render
from django.db.models.functions import ExtractYear
from .models import Awards


def ai_award(request):
    awards = Awards.objects.all().order_by('-award_dates')
    awards = Awards.objects.filter(team='AI')
    return render(request, 'labweb/award/ai_awards.html',
                  {
                      'award_list': awards
                  })

def hw_award(request):
    awards = Awards.objects.all().order_by('-award_dates')
    awards = Awards.objects.filter(team='HW')
    return render(request, 'labweb/award/hw_award.html',
                  {
                      'award_list': awards
                  })