from django.db import models
from accounts.models import BlogUser

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(BlogUser, on_delete=models.CASCADE, blank=True, null=True, related_name='post')
    
    def __str__(self):
        return self.title
    