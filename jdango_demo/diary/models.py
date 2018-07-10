from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    passwd = models.CharField(max_length=32)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Diary(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    budget = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    note = models.TextField()
    ddate = models.DateTimeField()

    def __str__(self):
        return "{} ({})".format(self.ddate, self.user)

class UserInfo(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    height = models.PositiveIntegerField(default=160)
    male = models.BooleanField(default=False)
    website = models.URLField(null=True)

    def __str__(self):
        return self.user.username
