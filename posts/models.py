from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'post/{self.pk}'

    def __str__(self):
        return self.title
