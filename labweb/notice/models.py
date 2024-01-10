from django.db import models
from member.models import member_list 

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(member_list, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()
    
    def __str__(self):
        return self.name
