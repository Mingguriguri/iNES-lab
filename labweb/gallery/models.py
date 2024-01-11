from django.db import models
import datetime

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=255, default="")
    upload_date = models.DateTimeField(default=datetime.datetime.now)
    contents = models.TextField(blank=True, null=True)
    photo_path = models.FileField(upload_to="upload/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "제목없음"
