from django.db import models

# Create your models here.
class Gallery(models.Model):
    photo_title = models.CharField(max_length=20)
    photo_dates = models.DateTimeField(blank = True, null = True)
    photo_context = models.CharField(max_length=100)
    photo_path = models.CharField(max_length=100, default="/static/brain.png")

    def __str__(self):
        return self.photo_title
