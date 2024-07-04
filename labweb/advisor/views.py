from django.shortcuts import render
from .models import Advisor

def advisor_list(request, team):
    advisors = Advisor.objects.filter(team=team.upper())
    team_name = "AI" if team.lower() == "ai" else "HW"
    for advisor in advisors:
        advisor.keywords_list = advisor.keywords.split(',')
    return render(request, 'labweb/advisor/advisor_list.html', 
                  {
                      'advisors': advisors, 
                      'team': team_name
                    })
