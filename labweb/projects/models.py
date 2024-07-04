from django.db import models

# Create your models here.
class article_list(models.Model):
    TEAM_CHOICES = (
        ('AI', 'AI Team'),
        ('HW', 'Hardware Team'),
    )
    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default='HW')

    article_name = models.CharField(max_length=150)
    article_dates = models.DateTimeField(blank = True, null = True)
    article_author = models.CharField(max_length=150, default="")
    article_keywords = models.CharField(max_length=150)
    article_abstract = models.CharField(max_length=1500)
    article_photo_path = models.CharField(max_length=100)
    article_architecture_path =  models.CharField(max_length=100, default="/static/brain.png")
    article_github = models.URLField(max_length=200, default="https://github.com/")
    article_paper_link = models.URLField(max_length=200, default="")

    def __str__(self):
        return self.article_name
