from django.db import models

# Create your models here.
class article_list(models.Model):
    article_name = models.CharField(max_length=150)
    article_dates = models.DateTimeField(blank = True, null = True)
    article_keywords = models.CharField(max_length=150)
    article_abstract = models.CharField(max_length=1500)
    article_photo_path = models.CharField(max_length=100)

    def __str__(self):
        return self.article_name
