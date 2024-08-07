from django.db import models
from area.models import Area
from project.models import Projects

# Create your models here.
class Publication(models.Model):
    TYPE_CHOICES = [
        ('CONF', 'Conference'),
        ('JOUR', 'Journal'),
        ('SURV', 'Survey'),
    ]

    TEAM_CHOICES = (
        ('AI', 'AI Team'),
        ('HW', 'Hardware Team'),
    )
    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default='HW')
    pub_type = models.CharField(max_length=4, choices=TYPE_CHOICES, default='JOUR')

    title = models.CharField(max_length=255)
    authors = models.TextField(blank=True)  # 참여하는 멤버들은 그냥 직접 작성하다는 점을 반영하여 TextField로 수정

    citation_text = models.TextField(blank=True)
    published_date = models.DateTimeField()
    doi_link = models.URLField()
    areas = models.ManyToManyField(Area, blank=True)  # 프로젝트 관련 영역
    pdf = models.FileField(upload_to='upload/publications/%Y/%m/%d/', null=True, blank=True)
    pdf_link = models.URLField(blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    related_project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='publications', null=True, blank=True)

    def __str__(self):
        return self.title