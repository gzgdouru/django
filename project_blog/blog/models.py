from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=64, null=True)
    register_time = models.DateTimeField(auto_now_add=True)
    fans_num = models.PositiveIntegerField(default=0)
    concern_num = models.PositiveIntegerField(default=0)
    master = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        if not self.nickname: self.nickname = self.username
        super(User, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=32)
    abstract = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=["views"])

    def save(self, *args, **kwargs):
        if not self.abstract: self.abstract = self.content[:32]
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return (reverse("blog:detail", args=(self.pk,)))

    class Meta:
        ordering = ["-created_time"]

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


