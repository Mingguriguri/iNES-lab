from django.db import models
from member.models import member_list 
from area.models import area
from publication.models import Journal, Conference

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    project_lead = models.ForeignKey(member_list, on_delete=models.CASCADE, related_name='project_lead')  # 프로젝트 리더
    members = models.ManyToManyField(member_list)  # 프로젝트에 참여하는 멤버들
    areas = models.ManyToManyField(area)  # 프로젝트 관련 영역
    publications = models.ManyToManyField(Journal, blank=True)  # 관련된 저널 출판물
    conferences = models.ManyToManyField(Conference, blank=True)  # 관련된 컨퍼런스 출판물

    def __str__(self):
        return self.name

