from django.db import models

# Create your models here.
class History(models.Model):
    history_title = models.CharField(max_length=100)
    history_dates = models.DateTimeField(blank = True, null = True)
    history_photo_path = models.CharField(max_length=100, default="/static/brain.png")

    def __str__(self):
        return self.history_title