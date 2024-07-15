from django.db import models
from users.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.TextField(max_length=1000)
    likes = models.IntegerField(default=0)