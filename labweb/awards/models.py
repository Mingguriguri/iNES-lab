from django.db import models
from member.models import member_list 

import datetime
# Create your models here.
class Awards(models.Model):
    TEAM_CHOICES = (
        ('AI', 'AI Team'),
        ('HW', 'Hardware Team'),
    )
    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default='HW')
    title = models.CharField(max_length=255, default="")
    award_dates = models.DateTimeField(default=datetime.datetime.now)
    contents = models.TextField(blank=True, null=True)
    photo = models.FileField(upload_to="upload/awards/%Y/%m/%d/", blank=True)
    award_link = models.URLField(blank=True, null=True)
    member = models.ManyToManyField(member_list)

    def __str__(self):
        return self.title if self.title else "제목없음"