from django.db import models
from users.models import User
from tweets.models import Tweet

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_liked = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    date_liked = models.DateField(auto_now_add=True)