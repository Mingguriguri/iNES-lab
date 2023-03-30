from django.db import models

# Create your models here.
class member_list(models.Model):
    name_text = models.CharField(max_length=20)
    ID_photo_path_text = models.CharField(max_length=100)