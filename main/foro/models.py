from django.db import models
from django.conf import settings

# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(max_length=300)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.title} - {self.author.username}'
    
class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} - {self.date_created}'