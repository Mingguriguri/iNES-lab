from django.db import models

# Create your models here.
class article_list(models.Model):
    article_name = models.CharField(max_length=50)
    article_keywords = models.CharField(max_length=50)
    article_abstract = models.CharField(max_length=350)
    article_photo_path = models.CharField(max_length=100)