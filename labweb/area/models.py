from django.db import models

# Create your models here.
class Area(models.Model):
    TEAM_CHOICES = (
        ('AI', 'AI Team'),
        ('HW', 'Hardware Team'),
    )
    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default='HW')
    area_name = models.CharField(max_length=150)
    area_description = models.TextField()
    photo = models.FileField(upload_to="upload/area/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.area_name
