from django.db import models

# Create your models here.
class Area(models.Model):
    area_name = models.CharField(max_length=150)
    area_description = models.TextField()
    photo = models.FileField(upload_to="upload/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.area_name
