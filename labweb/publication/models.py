from django.db import models

# Create your models here.
class Publication_list(models.Model):
    pub_name = models.CharField(max_length=50)
    pub_dates = models.DateTimeField("date published")
    pub_author = models.CharField(max_length=200)
    pub_photo_path = models.CharField(max_length=100)
    pub_pdf_path= models.CharField(max_length=100)

