from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text[:15]} {self.published_date.month}/{self.published_date.day}/{self.published_date.year}'

class Reply(Post):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')