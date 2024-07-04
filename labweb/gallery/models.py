from django.db import models
import datetime

# Create your models here.
class Gallery(models.Model):
    TEAM_CHOICES = (
        ('AI', 'AI Team'),
        ('HW', 'Hardware Team'),
    )
    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default='HW')
    title = models.CharField(max_length=255, default="")
    upload_date = models.DateTimeField(default=datetime.datetime.now)
    contents = models.TextField(blank=True, null=True)
    photo_path = models.FileField(upload_to="upload/%Y/%m/%d/", blank=True, null=True)
    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default='HW')

    def __str__(self):
        return self.title if self.title else "제목없음"
