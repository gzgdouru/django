from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey("blog.Post", on_delete=models.CASCADE) #删除关联数据是同时删除

    def __str__(self):
        return self.text[:20]