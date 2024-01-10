from django.db import models
from member.models import member_list 
from area.models import area

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    project_lead = models.ForeignKey(member_list, on_delete=models.CASCADE, related_name='project_lead')  # 프로젝트 리더
    members = models.ManyToManyField(member_list)  # 프로젝트에 참여하는 멤버들
    areas = models.ManyToManyField(area)  # 프로젝트 관련 영역
    
    def __str__(self):
        return self.name

