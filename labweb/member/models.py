from django.db import models

# Create your models here.
class member_list(models.Model):
    name_text = models.CharField(max_length=20)
    one_sentence_text = models.CharField(max_length=50, default="Good, better, best")
    ID_photo_path_text = models.CharField(max_length=100)
    second_photo_path = models.CharField(max_length=100, default="/static/brain.png")
    degree = models.CharField(max_length=50, default = "M.S. student")
    email = models.EmailField(max_length=254, default="@gachon.ac.kr")
    department = models.CharField(max_length=50, default = "Department of Biomedical Engineering")
    
    def __str__(self):
        return self.name_text
