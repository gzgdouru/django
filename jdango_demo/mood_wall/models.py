from django.db import models

# Create your models here.
class Mood(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.status

class Post(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=32, default="不愿透漏身份的人")
    message = models.TextField()
    del_pass = models.CharField(max_length=10, null=True)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.message
