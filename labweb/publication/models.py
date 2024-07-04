from django.db import models

# Create your models here.
class Journal(models.Model):
    TEAM_CHOICES = (
        ('AI', 'AI Team'),
        ('HW', 'Hardware Team'),
    )
    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default='HW')
    pub_name = models.CharField(max_length=150, unique=True)
    pub_dates = models.DateTimeField("date published")
    pub_author = models.CharField(max_length=200)
    pub_publisher = models.CharField(max_length=200, blank = True, null = True)
    pub_pdf_path= models.CharField(max_length=100)


    def __str__(self):
        return self.pub_name

class Conference(models.Model):
    TEAM_CHOICES = (
        ('AI', 'AI Team'),
        ('HW', 'Hardware Team'),
    )
    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default='HW')
    conf_name = models.CharField(max_length=150, unique=True)
    conf_dates = models.DateTimeField("date published")
    conf_author = models.CharField(max_length=200)
    conf_publisher = models.CharField(max_length=200, blank = True, null = True)
    conf_pdf_path= models.CharField(max_length=100)

    def __str__(self):
        return self.conf_name