from django.db import models

# Create your models here.
class area(models.Model):
    area_name = models.CharField(max_length=150)
    area_description = models.TextField()

    def __str__(self):
        return self.area_name
