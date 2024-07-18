import datetime
from django.db import models
from member.models import member_list
from area.models import Area

class Projects(models.Model):
    TEAM_CHOICES = (
        ('AI', 'AI Team'),
        ('HW', 'Hardware Team'),
    )
    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default='HW')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Abstract으로 사용
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(default=datetime.datetime.now)
    project_lead = models.ForeignKey(member_list, on_delete=models.CASCADE, related_name='project_lead', blank=True, null=True)  # 프로젝트 리더
    members = models.ManyToManyField(member_list)  # 프로젝트에 참여하는 멤버들
    areas = models.ManyToManyField(Area, blank=True, null=True)  # 프로젝트 관련 영역
    keywords = models.CharField(max_length=255, blank=True, null=True)  # 키워드 필드
    github_link = models.URLField(max_length=200, blank=True, null=True)  # GitHub 링크
    paper_link = models.URLField(max_length=200, blank=True, null=True)  # 논문 링크
    other_link = models.URLField(max_length=200, blank=True, null=True)  # 기타 링크

    def __str__(self):
        return self.name

# 여러 파일 관리
class ProjectPhoto(models.Model):
    project = models.ForeignKey(Projects, related_name='photos', on_delete=models.CASCADE)
    photo = models.FileField(upload_to='upload/project/%Y/%m/%d/')

    def __str__(self):
        return f"Photo for {self.project.name}"
