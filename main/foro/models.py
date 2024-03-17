from django.db import models
from django.conf import settings

# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} - {self.author.username}'


    
class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} - {self.date_created}'