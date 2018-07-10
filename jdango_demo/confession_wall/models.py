from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile_user", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=32, default="匿名用户")
    male = models.BooleanField(default=False)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nickname

class Post(models.Model):
    user = models.ForeignKey(User, related_name="post_user", on_delete=models.CASCADE)
    context = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

