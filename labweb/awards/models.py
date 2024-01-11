from django.db import models
from member.models import member_list 

import datetime
# Create your models here.
class Awards(models.Model):
    title = models.CharField(max_length=255)
    award_dates = models.DateTimeField(default=datetime.datetime.now)
    contents = models.TextField(blank=True, null=True)
    photo = models.FileField(upload_to="upload/%Y/%m/%d/", blank=True)
    award_link = models.URLField(blank=True, null=True)
    member = models.ManyToManyField(member_list)

    def __str__(self):
        return self.awards_title