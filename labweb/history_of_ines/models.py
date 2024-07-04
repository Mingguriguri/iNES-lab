from django.db import models
import datetime

class History(models.Model):
    TEAM_CHOICES = (
        ('AI', 'AI Team'),
        ('HW', 'Hardware Team'),
    )
    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default='HW')
    title = models.CharField(max_length=255)
    history_date = models.DateTimeField(default=datetime.datetime.now)    
    description = models.TextField(null=True, blank=True)
    photo = models.FileField(upload_to="upload/%Y/%m/%d/", blank=True)
    #award = models.ForeignKey(Awards, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title