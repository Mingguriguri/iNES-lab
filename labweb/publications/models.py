from django.db import models
from project.models import Projects

# Create your models here.
class Publication(models.Model):
    TYPE_CHOICES = [
        ('CONF', 'Conference'),
        ('JOUR', 'Journal'),
        ('SURV', 'Survey'),
    ]
    title = models.CharField(max_length=255)
    citation_text = models.TextField()
    published_date = models.DateTimeField()
    doi_link = models.URLField()
    pub_type = models.CharField(max_length=4, choices=TYPE_CHOICES, default='JOUR')
    related_project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.name