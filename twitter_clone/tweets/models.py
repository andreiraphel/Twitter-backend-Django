from django.db import models
from users.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.TextField(max_length=1000)
    tweet_created = models.DateTimeField(auto_now_add=True, null=True)
    type = models.CharField(max_length=10, default='tweet')