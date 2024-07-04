from django.db import models

class EducationExperience(models.Model):
    advisor = models.ForeignKey('Advisor', on_delete=models.CASCADE, related_name='education_experiences')
    date_range = models.CharField(max_length=200)  # 날짜 범위
    institution = models.CharField(max_length=255)  # 학교/기관
    position = models.CharField(max_length=255)  # 직책

    def __str__(self):
        return f"{self.institution} ({self.date_range})"

class Advisor(models.Model):
    TEAM_CHOICES = (
        ('AI', 'AI Team'),
        ('HW', 'HW Team'),
    )

    team = models.CharField(max_length=2, choices=TEAM_CHOICES, default='AI')
    name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=200)  # 소속
    position = models.CharField(max_length=200)  # 직위
    research_fields = models.TextField(blank=True, null=True)  # 연구분야
    lab_location = models.CharField(max_length=200)  # 연구실위치
    specialty = models.CharField(max_length=200, blank=True, null=True)  # 전공분야
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    fax = models.CharField(max_length=20, blank=True, null=True)
    introduction = models.TextField()  # 소개
    keywords = models.TextField()  # 키워드
    photo = models.FileField(upload_to="upload/advisor_photos/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return self.name