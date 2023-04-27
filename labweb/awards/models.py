from django.db import models

# Create your models here.
class Awards(models.Model):
    awards_title = models.CharField(max_length=150)
    award_dates = models.DateTimeField(blank = True, null = True)
    awrad_contents = models.CharField(max_length=3000)
    award_photo_path = models.CharField(max_length=100)