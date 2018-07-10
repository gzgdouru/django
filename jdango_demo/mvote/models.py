from django.db import models

# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PollItem(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200, blank=True, null=True)
    vote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class VoteChech(models.Model):
    userid = models.PositiveIntegerField()
    pollid = models.PositiveIntegerField()
    vote_date = models.DateField()
