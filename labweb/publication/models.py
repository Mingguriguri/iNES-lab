from django.db import models

# Create your models here.
class Publication_list(models.Model):
    pub_name = models.CharField(max_length=150, unique=True)
    pub_dates = models.DateTimeField("date published")
    pub_author = models.CharField(max_length=200)
    pub_publisher = models.CharField(max_length=200, blank = True, null = True)
    pub_pdf_path= models.CharField(max_length=100)

    def __str__(self):
        return self.pub_name
