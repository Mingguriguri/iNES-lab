from django.db import models

# Create your models here.
class member_list(models.Model):
    # 옵션 선택
    DEGREE_CHOICES = [
        # DB에 실제로 저장되는 값 (공간절약) / admin site or form에서 보여지는 모습
        ('CA', 'Co-Advisor'),
        ('PR', 'Professor'),
        ('PD', 'Postdoc'),
        ('PHD', 'PhD'),
        ('MS', 'Master'),
        ('BS', 'Bachelor'),      
    ]

    STATUS_CHOICES = [
        ('CU', 'Current'),
        ('AL', 'Alumni'),
    ]
    name = models.CharField(max_length=20, default="Name")
    email = models.EmailField(max_length=254, default="@gachon.ac.kr")
    main_photo = models.FileField(upload_to="uploads/%Y/%m/%d/", blank=True)
    hobby_photo = models.FileField(upload_to="uploads/%Y/%m/%d/", blank=True)
    main_photo_path_text = models.CharField(max_length=100)
    hobby_photo_path = models.CharField(max_length=100, default="/static/brain.png")
    motto = models.CharField(max_length=50, default="Good, better, best")
    department = models.CharField(max_length=50, default = "Department of Biomedical Engineering")
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, default='BS')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='CU')

    def __str__(self):
        return self.name
