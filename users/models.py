from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='profile_images/', default='default_pic.jpg')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return self.user.username

